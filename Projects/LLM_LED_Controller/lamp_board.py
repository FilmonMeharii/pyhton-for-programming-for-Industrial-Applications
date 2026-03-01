from __future__ import annotations

import json
import queue
import socket
import threading
import tkinter as tk
from tkinter import ttk
from typing import Dict, List, Tuple

HOST = "127.0.0.1"
PORT = 8765


# ---------------------------
# Server (TCP + newline JSON)
# ---------------------------
state_lock = threading.Lock()
clients_lock = threading.Lock()

STATE: Dict[str, bool] = {"led1": False, "led2": False, "led3": False}
CLIENTS: List[socket.socket] = []


def _send_json(sock: socket.socket, obj: dict) -> None:
    sock.sendall((json.dumps(obj) + "\n").encode("utf-8"))


def _broadcast_state() -> None:
    with state_lock:
        msg = {"type": "state", **STATE}

    dead: List[socket.socket] = []
    with clients_lock:
        for c in CLIENTS:
            try:
                _send_json(c, msg)
            except OSError:
                dead.append(c)

        for d in dead:
            try:
                CLIENTS.remove(d)
            except ValueError:
                pass
            try:
                d.close()
            except OSError:
                pass


def _handle_client(conn: socket.socket, addr: Tuple[str, int]) -> None:
    with clients_lock:
        CLIENTS.append(conn)

    # send initial state
    try:
        _broadcast_state()
    except Exception:
        pass

    f = conn.makefile("r", encoding="utf-8", newline="\n")
    try:
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                msg = json.loads(line)
                if not isinstance(msg, dict):
                    raise ValueError("Message must be a JSON object")
            except Exception as e:
                try:
                    _send_json(conn, {"type": "error", "message": f"Bad JSON: {e}"})
                except OSError:
                    break
                continue

            mtype = msg.get("type")
            if mtype == "get":
                with state_lock:
                    _send_json(conn, {"type": "state", **STATE})

            elif mtype == "set":
                # require all keys for simplicity
                if not all(k in msg for k in ("led1", "led2", "led3")):
                    _send_json(conn, {"type": "error", "message": "set requires led1, led2, led3"})
                    continue
                if not all(isinstance(msg[k], bool) for k in ("led1", "led2", "led3")):
                    _send_json(conn, {"type": "error", "message": "led1/2/3 must be booleans"})
                    continue

                with state_lock:
                    STATE["led1"] = msg["led1"]
                    STATE["led2"] = msg["led2"]
                    STATE["led3"] = msg["led3"]

                _broadcast_state()

            else:
                _send_json(conn, {"type": "error", "message": f"Unknown type: {mtype!r}"})

    except Exception:
        pass
    finally:
        try:
            f.close()
        except Exception:
            pass

        with clients_lock:
            if conn in CLIENTS:
                CLIENTS.remove(conn)

        try:
            conn.close()
        except OSError:
            pass


def start_server(stop_event: threading.Event, server_ready: threading.Event) -> None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen()

            server_ready.set()  # ✅ signal that we're listening

            print(f"LED Server running on {HOST}:{PORT}")
            s.settimeout(0.5)

            while not stop_event.is_set():
                try:
                    conn, addr = s.accept()
                except socket.timeout:
                    continue
                t = threading.Thread(target=_handle_client, args=(conn, addr), daemon=True)
                t.start()

    except OSError as e:
        # Common: [Errno 98] Address already in use (Linux/macOS) or WinError 10048 (Windows)
        print(f"[SERVER ERROR] Could not start server on {HOST}:{PORT}: {e}")
        server_ready.set()  # unblock main so it can exit gracefully



# ---------------------------
# Tkinter HMI
# ---------------------------
def _client_send(sock: socket.socket, lock: threading.Lock, obj: dict) -> None:
    with lock:
        _send_json(sock, obj)


class LedTile(ttk.Frame):
    def __init__(self, master: tk.Misc, title: str, on_on, on_off):
        super().__init__(master, padding=10)

        ttk.Label(self, text=title, font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w")

        self.canvas = tk.Canvas(self, width=60, height=60, highlightthickness=0)
        self.canvas.grid(row=0, column=1, rowspan=2, padx=(12, 0))
        self.oval = self.canvas.create_oval(8, 8, 52, 52, outline="#222", width=2)

        self.status = ttk.Label(self, text="OFF", font=("Segoe UI", 10))
        self.status.grid(row=1, column=0, sticky="w", pady=(2, 0))

        btns = ttk.Frame(self)
        btns.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 0))
        btns.columnconfigure((0, 1), weight=1)

        ttk.Button(btns, text="ON", command=on_on).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        ttk.Button(btns, text="OFF", command=on_off).grid(row=0, column=1, sticky="ew", padx=(6, 0))

        self.set_state(False)

    def set_state(self, on: bool) -> None:
        if on:
            self.canvas.itemconfig(self.oval, fill="#2ecc71")
            self.status.config(text="ON")
        else:
            self.canvas.itemconfig(self.oval, fill="#555555")
            self.status.config(text="OFF")


class LampServerHMI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lamp Board (Server + HMI)")
        self.geometry("540x600")
        self.minsize(540, 600)

        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass

        self.sock = socket.create_connection((HOST, PORT), timeout=5)
        self.sock.settimeout(None)  # important: make reads block forever (no TimeoutError)
        self.sock_lock = threading.Lock()

        self.in_q: "queue.Queue[dict]" = queue.Queue()
        self.state = {"led1": False, "led2": False, "led3": False}

        root = ttk.Frame(self, padding=16)
        root.pack(fill="both", expand=True)

        ttk.Label(root, text="Lamp Board HMI", font=("Segoe UI", 16, "bold")).pack(anchor="w")
        ttk.Label(root, text=f"Server: {HOST}:{PORT}", font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 12))

        self.led1 = LedTile(root, "LED 1", lambda: self._set_led("led1", True), lambda: self._set_led("led1", False))
        self.led2 = LedTile(root, "LED 2", lambda: self._set_led("led2", True), lambda: self._set_led("led2", False))
        self.led3 = LedTile(root, "LED 3", lambda: self._set_led("led3", True), lambda: self._set_led("led3", False))

        self.led1.pack(fill="x", pady=6)
        self.led2.pack(fill="x", pady=6)
        self.led3.pack(fill="x", pady=6)

        self.status = ttk.Label(root, text="Connecting...", font=("Segoe UI", 9))
        self.status.pack(anchor="w", pady=(10, 0))

        threading.Thread(target=self._reader_thread, daemon=True).start()

        # request initial state
        _client_send(self.sock, self.sock_lock, {"type": "get"})

        self.after(50, self._ui_tick)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _reader_thread(self) -> None:
        f = self.sock.makefile("r", encoding="utf-8", newline="\n")
        try:
            while True:
                try:
                    line = f.readline()
                except TimeoutError:
                    continue  # just try again

                if not line:
                    break

                line = line.strip()
                if not line:
                    continue

                try:
                    msg = json.loads(line)
                    if isinstance(msg, dict):
                        self.in_q.put(msg)
                except Exception:
                    pass
        finally:
            try:
                f.close()
            except Exception:
                pass


    def _set_led(self, key: str, value: bool) -> None:
        self.state[key] = value
        _client_send(self.sock, self.sock_lock, {"type": "set", **self.state})

    def _ui_tick(self) -> None:
        while True:
            try:
                msg = self.in_q.get_nowait()
            except queue.Empty:
                break

            if msg.get("type") == "state":
                self.state["led1"] = bool(msg.get("led1", False))
                self.state["led2"] = bool(msg.get("led2", False))
                self.state["led3"] = bool(msg.get("led3", False))

                self.led1.set_state(self.state["led1"])
                self.led2.set_state(self.state["led2"])
                self.led3.set_state(self.state["led3"])
                self.status.config(text="State updated")

            elif msg.get("type") == "error":
                self.status.config(text=f"Server error: {msg.get('message')}")

        self.after(50, self._ui_tick)

    def _on_close(self) -> None:
        try:
            self.sock.close()
        except Exception:
            pass
        self.destroy()


def main() -> None:
    stop_event = threading.Event()
    server_ready = threading.Event()

    server_thread = threading.Thread(
        target=start_server,
        args=(stop_event, server_ready),
        daemon=True
    )
    server_thread.start()

    # ✅ Wait until server has bound+listened (or failed)
    server_ready.wait()

    # Now start HMI (connects to server)
    try:
        app = LampServerHMI()
        app.mainloop()
    finally:
        stop_event.set()



if __name__ == "__main__":
    main()
