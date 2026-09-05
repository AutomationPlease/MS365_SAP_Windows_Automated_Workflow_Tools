import time
import ctypes
import traceback
import random
from datetime import datetime

#Add windows constants
ES_CONTINUOUS           = 0x80000000
ES_DISPLAY_REQUIRED     = 0x00000002
ES_SYSTEM_REQUIRED      = 0x00000001

MOUSEEVENTF_MOVE        = 0x0001

INTERVAL                = 180       #3 minutes between activity
PREVENT_RECALL_INTERVAL = 30        #Reapply sleep prevention every 30s
MAX_MOVE                = 6         #Small mouse movement

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("keep_alive.log", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp} | {message}\n")
    except:
        pass

def prevent_sleep():
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED
        )
        log("Sleep prevention activated.")
    except Exception as e:
        log(f"Failed to prevent sleep: {e}")

def allow_sleep():
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        log("Sleep settings restored.")
    except:
        pass

def jiggle_mouse():
    try:
        dx = random.randint(-MAX_MOVE, MAX_MOVE)
        dy = random.randint(-MAX_MOVE, MAX_MOVE)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)
        return True
    except:
        return False

log("=== Keep Alive Started ===")

try:
    prevent_sleep()
    
    last_prevent = time.time()
    next_action = time.time() + INTERVAL

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        jiggle_mouse()
        log(f"Mouse jiggled at {current_time}")
        
        #reapply sleep prevention periodically
        if time.time() - last_prevent >= PREVENT_RECALL_INTERVAL:
            prevent_sleep()
            last_prevent = time.time()
        
        #Get accurate time, slighty account for drift
        now = time.time()
        sleep_time = next_action - now
        if sleep_time > 0:
            time.sleep(sleep_time)
        next_action += INTERVAL

except KeyboardInterrupt:
    log("Keyboard interrupt received. Stopping...")
    allow_sleep()
except Exception as e:
    log(f"CRITICAL ERROR: {e}")
    log(traceback.format_exc())
    allow_sleep()
finally:
    log("Script terminated cleanly.")
