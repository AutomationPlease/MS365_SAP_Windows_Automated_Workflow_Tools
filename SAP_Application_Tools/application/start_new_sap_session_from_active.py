import time
import win32com.client

#Connect to active SAP session and minmize main session window
SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)
original_session.findByID("wnd[0]").iconify() #i usually keep the main session minimized with simulated activity going to keep active
old_count = connection.Sessions.Count

#create second session window
session.createSession()

#establish new session based off current session window count, maximize new session window
new_session = connection.Sessions(connection.Sessions.Count - 1)
new_session.findByID("wnd[0]").maximize() #or can use .iconify() to minimize the new session window
time.sleep(1.5)

#example of going to specific tcode in new session window, change tcode name to tcode of choice
new_session.findById("wnd[0]/tbar[0]/okcd").text = "tcode_name"
new_session.findById("wnd[0]/tbar[0]/btn[0]").press()
