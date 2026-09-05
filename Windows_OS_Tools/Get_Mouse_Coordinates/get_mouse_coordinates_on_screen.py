import pyautogui
import time

#move your mouse to the desired position
#prints after 5 seconds

for i in range(5, 0, -1):
    print(f"{i}...", end=" ", flush=True)
    time.sleep(1)

x, y = pyautogui.position()

print(f"x = {x}")
print(f"y = {y}")
