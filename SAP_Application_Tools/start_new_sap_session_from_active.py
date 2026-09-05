import time
import win32gui, win32con, win32com.client
import time
import win32com.client as win32, win32gui, win32con, win32com

#Connect to active SAP session and minmize main session window
SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)
original_session.findByID("wnd[0]").iconify()
old_count = connection.Sessions.Count

#create second session window
session.createSession()

#raise error flag if new session is not created
deadline = time.time() + 15
while connection.Sessions.Count <= old_count:
    if time.time() > deadline:
        raise TimeoutError("New SAP session not created.")
    time.sleep(0.2)

#establish new session, maximize new session window
new_session = connection.Sessions(connection.Sessions.Count - 1)
new_session.findByID("wnd[0]").maximize()
time.sleep(1.5)
