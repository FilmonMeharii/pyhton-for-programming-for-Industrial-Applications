import json
import socket
import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3:8b"

HOST = "127.0.0.1"
PORT = 8765

SYSTEM_INSTRUCTIONS = """
You control three LEDs: led1, led2, led3.

You MUST reply with ONLY a single JSON object.
No markdown. No extra text. No explanations outside the JSON.

Required JSON format (always include all keys):
{
  "led1": true|false,
  "led2": true|false,
  "led3": true|false,
  "message": "short message to the user"
}

Rules:
- Use true/false booleans (not strings like "true")
- If user asks something unclear, keep LEDs unchanged and explain in "message"
- Be helpful and friendly in your message
- Always respond with valid JSON only
"""

def send_json(sock: socket.socket, obj: dict) -> None:
    sock.sendall((json.dumps(obj) + "\n").encode("utf-8"))

def recv_json_line(sock: socket.socket) -> dict:
    f = sock.makefile("r", encoding="utf-8", newline="\n")
    line = f.readline()
    if not line:
        raise ConnectionError("Server closed connection")
    return json.loads(line.strip())

def get_state(sock: socket.socket) -> dict:
    send_json(sock, {"type": "get"})
    while True:
        msg = recv_json_line(sock)
        if msg.get("type") == "state":
            return {
                "led1": bool(msg["led1"]),
                "led2": bool(msg["led2"]),
                "led3": bool(msg["led3"]),
            }

def set_state(sock: socket.socket, state: dict) -> None:
    send_json(sock, {"type": "set", **state})

def call_llm(user_text: str, current_state: dict) -> dict:
    prompt = (
        f"{SYSTEM_INSTRUCTIONS}\n\n"
        f"Current LED state:\n{json.dumps(current_state)}\n\n"
        f"User says: {user_text}\n"
    )
    
    print(f"Sending to AI: '{user_text}'")
    
    r = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=120,
    )
    r.raise_for_status()
    
    content = r.json()["response"]
    
    print("\n--- RAW AI OUTPUT ---")
    print(content)
    print("----------------------\n")
    
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"AI didn't return valid JSON: {e}")
        return {**current_state, "message": "Sorry, I had trouble understanding."}
    
    for k in ("led1", "led2", "led3", "message"):
        if k not in data:
            raise ValueError(f"Missing key: {k}")
    
    if not all(isinstance(data[k], bool) for k in ("led1", "led2", "led3")):
        raise ValueError("led1/led2/led3 must be booleans")
    
    return data

# Simple test of AI without Lamp Board
if __name__ == "__main__":
    print("Testing AI connection...")
    
    test_state = {"led1": False, "led2": False, "led3": False}
    
    result = call_llm("turn on the first LED", test_state)
    
    print("AI Response:")
    print(f"   LED1: {result['led1']}")
    print(f"   LED2: {result['led2']}")
    print(f"   LED3: {result['led3']}")
    print(f"   Message: {result['message']}")

def main():
    """Main chat loop - connects everything together!"""
    
    # Connect to Lamp Board
    try:
        sock = socket.create_connection((HOST, PORT), timeout=5)
        sock.settimeout(None)
        print("Connected to Lamp Board!")
        print("Type your commands (or 'quit' to exit)\n")
    except Exception as e:
        print(f"Could not connect to Lamp Board: {e}")
        print("   Make sure lamp_board.py is running!")
        return
    
    try:
        while True:
            # Get user input
            user_text = input("> ").strip()
            
            # Check if user wants to quit
            if user_text.lower() in ("quit", "exit", "q"):
                print("Goodbye!")
                break
            
            # Skip empty input
            if not user_text:
                continue
            
            # Get current LED state from Lamp Board
            current_state = get_state(sock)
            print(f"Current: {current_state}")
            
            # Ask AI what to do
            try:
                result = call_llm(user_text, current_state)
            except Exception as e:
                print(f"AI Error: {e}")
                continue
            
            # Extract new LED states and message
            new_state = {
                "led1": result["led1"],
                "led2": result["led2"],
                "led3": result["led3"]
            }
            
            # Apply the new states to Lamp Board
            set_state(sock, new_state)
            print(f"Changed to: {new_state}")
            
            # Show AI's message
            print(f"AI says: {result['message']}\n")
            
    finally:
        # Always close the connection
        sock.close()
        print("Disconnected from Lamp Board")


if __name__ == "__main__":
    main()