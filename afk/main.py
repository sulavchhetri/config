import pyautogui
import random
import time
import sys

print("Anti-AFK started. Press Ctrl+C to stop.\n")

try:
    while True:
        # Get current mouse position
        x, y = pyautogui.position()
        
        # Move cursor a small random distance
        dx = random.randint(-50, 50)
        dy = random.randint(-50, 50)
        pyautogui.moveTo(x + dx, y + dy, duration=0.2)
        
        # Random sleep time between moves
        sleep_time = random.randint(30, 120)
        print(f"Moved mouse, next move in {sleep_time}s")

        # Countdown timer
        for remaining in range(sleep_time, 0, -1):
            sys.stdout.write(f"\rNext move in: {remaining:3d}s ")
            sys.stdout.flush()
            time.sleep(1)
        print()  # Move to a new line after countdown completes

except KeyboardInterrupt:
    print("\nStopped.")

