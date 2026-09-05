"""
Add within SAP automation scripts, after connection block, to minimize system logon pad.
Most SAP systems logon pad is called something like "SAP Logon 800".
"""

import win32gui, win32con, win32com.client

def close_logon_pad():
    def enum_callback(hwnd, _):
        title = win32gui.GetWindowText(hwnd).upper()
        if "SAP Logon 800" in title or "SAP Logon" in title or "800" in title:
            if win32gui.IsWindowVisible(hwnd):
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    win32gui.EnumWindows(enum_callback, None)
