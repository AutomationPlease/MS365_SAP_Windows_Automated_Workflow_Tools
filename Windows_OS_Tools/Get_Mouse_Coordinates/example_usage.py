#add imports if not already being used
import pyautogui
import time

#... rest of your main automation script goes here ...

if application_is_not_responding():
    print("Application/window frozen - attempting force close...")
    
    #coordinates captured from get_mouse_coordinates_on_screen.py, numbers shown below are hypothetical
    x = 1342
    y = 756
    
    pyautogui.click(x, y)        #click "Force Close" or "End Task" button
    time.sleep(2)
    
    print("Force close attempted.")

#... rest of your main automation script continues ...
