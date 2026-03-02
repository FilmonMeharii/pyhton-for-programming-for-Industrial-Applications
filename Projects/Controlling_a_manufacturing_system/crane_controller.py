from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import time
import json
from collections import deque

# Queue system for managing parts
part_queue = deque()  # Queue to store parts waiting to be processed
last_part_count = 0  # Track last known part count at source 1

# Read a value from a Modbus address
def read_input(address):
    result = client.read_holding_registers(address=address, count=1)
    return result.registers[0]

# Write a value to a Modbus address
def write_output(address, value):
    result = client.write_register(address, value)
    print(f"Successfully wrote {value} to address {address}")
    return result

def move_to(x, y):
    print(f"Moving crane to X: {x}, Y: {y}...")
    
    # Set y position first for safety
    write_output(2, y)  # Address 2 = Target Y position
    time.sleep(0.5)

    # Set x position
    write_output(1, x)  # Address 1 = Target X position
    time.sleep(2)  # Wait for the crane to move

    # Verify position
    current_x = read_input(15)
    current_y = read_input(16)
    print(f"Current position after move: X={current_x}, Y={current_y}")

def vacuum_on():
    print("Turning vacuum ON...")
    write_output(3, 1)  # Address 3 = Vacuum control (1=ON)
    time.sleep(1)
    print("Vacuum is now ON.")

def vacuum_off():
    print("Turning vacuum OFF...")
    write_output(3, 0)  # Address 3 = Vacuum control (0=OFF)
    time.sleep(1)
    print("Vacuum is now OFF.")

def execute_actions(actions):
    """Execute a sequence of actions from a JSON path file"""
    for i, action in enumerate(actions):
        print(f"Executing action {i+1}: {action.get('description', 'No description')}")
        if 'setX' in action and 'setY' in action:
            move_to(action['setX'], action['setY'])
        elif 'vacuum' in action:
            if action['vacuum'] == 1:
                vacuum_on()
            else:
                vacuum_off()
        else:
            print(f"Unknown action: {action}")

        time.sleep(0.5)

def load_json_path(filename):
    """Load a path configuration from JSON file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

def check_for_new_parts():
    """Check if new parts have been generated at Source 1"""
    global last_part_count
    
    # Read Source 1 sensor (Address 17 = Source1 sensor)
    try:
        source1_sensor = read_input(17)
        if source1_sensor == 1 and last_part_count == 0:
            print(f"[QUEUE] Detected part at Source 1")
            part_queue.append({'type': 1, 'source': 'Source1'})
            last_part_count = 1
        elif source1_sensor == 0:
            last_part_count = 0
    except Exception as e:
        print(f"Warning: Could not read part sensor from Source 1: {e}")

def process_queue():
    """Process parts in the queue through Source1 -> Process1 -> Sink"""
    if not part_queue:
        return False
    
    part = part_queue.popleft()
    print(f"\n[QUEUE] Processing {part['type']}: {part['source']} -> Process1 -> Sink")
    print("="*50)
    
    # Load and execute Source 1 to Process 1 path
    path_s1_p1 = load_json_path('path_source1_to_process1.json')
    if path_s1_p1:
        print(f"Executing: {path_s1_p1['description']}")
        execute_actions(path_s1_p1['actions'])
    
    # Load and execute Process 1 to Sink path
    path_p1_sink = load_json_path('path_process1_to_sink.json')
    if path_p1_sink:
        print(f"Executing: {path_p1_sink['description']}")
        execute_actions(path_p1_sink['actions'])
    
    print("="*50)
    print(f"[QUEUE] Part delivery completed. Queue size: {len(part_queue)}\n")
    return True

def main():
    """Main control loop for the crane system"""
    global client
    
    # Connect to the simulation
    client = ModbusTcpClient('127.0.0.1')
    client.connect()
    print("Connected to crane simulation!")
    print("="*50)
    
    try:
        # Initialize the system
        print("Initializing crane control system...")
        vacuum_off()
        move_to(55, 200)  # Move to safe position above Source 1
        
        print("Crane system ready. Monitoring for parts...")
        print("="*50)
        
        # Main event loop
        while True:
            # Check for new parts at Source 1
            check_for_new_parts()
            
            # Process parts in queue
            if part_queue:
                process_queue()
            else:
                # Idle state
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("\n[SYSTEM] Shutdown signal received...")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        # Cleanup
        print("[SYSTEM] Returning crane to safe position...")
        try:
            vacuum_off()
            move_to(55, 200)
        except:
            pass
        
        client.close()
        print("[SYSTEM] Disconnected from crane simulation.")
        print(f"[SYSTEM] Total parts processed: {len(part_queue) == 0}")

if __name__ == "__main__":
    main() 