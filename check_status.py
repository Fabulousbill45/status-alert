import time
import requests
import ctypes
import winsound
from datetime import datetime

def alert(title, text):
    # Play a sequence of beeps to get attention
    for _ in range(3):
        winsound.Beep(1000, 500)
        time.sleep(0.1)
    
    # Show an alert dialog box that stays on top
    MB_OK = 0x0
    MB_ICONINFORMATION = 0x40
    MB_SYSTEMMODAL = 0x1000
    
    ctypes.windll.user32.MessageBoxW(0, text, title, MB_OK | MB_ICONINFORMATION | MB_SYSTEMMODAL)

def main():
    url = "https://status.geforcenow.com/api/v2/status.json"
    
    print("=" * 50)
    print("GeForce NOW Status Checker")
    print("Checking every 30 minutes. Keep this window open.")
    print("You will be alerted with a sound and popup when all systems are operational.")
    print("=" * 50)
    
    while True:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            indicator = data.get("status", {}).get("indicator", "unknown")
            description = data.get("status", {}).get("description", "Unknown Status")
            
            current_time = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
            print(f"[{current_time}] Current Status: {indicator.upper()} - {description}")
            
            if indicator == "none" or description.lower() == "all systems operational":
                print(f"[{current_time}] SERVERS ARE BACK UP!")
                alert("GeForce NOW Alert", "The GeForce NOW servers appear to be back up!\n\nStatus: All Systems Operational.")
                break
                
        except Exception as e:
            current_time = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
            print(f"[{current_time}] Error checking status: {e}")
            
        time.sleep(30 * 60)

if __name__ == "__main__":
    main()
