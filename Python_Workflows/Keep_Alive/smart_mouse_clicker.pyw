import time
import ctypes
import traceback
import random
from datetime import datetime

#Mouse constants
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

INTERVAL = 90
CLICK_CHANCE = 1.0

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("mouse_clicker.log", "a", encoding="utf-8") as f:
            f.write(f"{timestamp} | {message}\n")
    except:
        pass
    print(f"{timestamp} | {message}")

def get_screen_size():
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)
    return width, height

def move_mouse_absolute(x, y):
    try:
        screen_width, screen_height = get_screen_size()
        #Convert pixels to 0-65535 scale (required by Windows)
        cx = int(x * 65535 / screen_width)
        cy = int(y * 65535 / screen_height)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, cx, cy, 0, 0)
    except Exception as e:
        log(f"Move failed: {e}")

def left_click():
    try:
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.06)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    except:
        pass

log("=== Smart Mouse Clicker Started ===")

try:
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        screen_w, screen_h = get_screen_size()
        
        #Go to blank area in lower-right of screen
        blank_x = random.randint(int(screen_w * 0.70), screen_w - 80)
        blank_y = random.randint(int(screen_h * 0.60), screen_h - 120)
        
        move_mouse_absolute(blank_x, blank_y)
        time.sleep(0.25)
        
        #Click
        if random.random() < CLICK_CHANCE:
            left_click()
            log(f"{current_time} | Clicked blank space at ({blank_x}, {blank_y})")
        
        #Return to random safe location on screen
        return_x = random.randint(100, screen_w - 100)
        return_y = random.randint(100, screen_h - 100)
        move_mouse_absolute(return_x, return_y)
        
        log(f"Returned to random position ({return_x}, {return_y})")
        
        #Random sleep
        sleep_time = INTERVAL + random.randint(-20, 35)
        if sleep_time < 40:
            sleep_time = 40
        time.sleep(sleep_time)

except KeyboardInterrupt:
    log("Stopping...")
except Exception as e:
    log(f"ERROR: {e}")
    log(traceback.format_exc())
finally:
    log("Terminated.")
    input("\nPress Enter to close...")
