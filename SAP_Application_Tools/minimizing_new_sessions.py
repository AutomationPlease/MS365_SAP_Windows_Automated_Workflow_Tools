"""
Basic SAP GUI connection block, and example flow for minimizing sessions, and creating new sessions.
You can have up to 5 active GUI window sessions.
"""

import win32com.client
import time

SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
original_session = connection.Children(0)

#Minimize main logged in window with iconify
original_session.findByID("wnd[0]").iconify()
print("Minimized main system session:", original_session.Info.SessionNumber)

#Create second session
original_session.createSession()
time.sleep(1.5)

#Get the newly created session and minimize it
second_session = connection.Sessions(connection.Sessions.Count - 1)
second_session.findByID("wnd[0]").iconify()
print("Minimized second session window:", second_session.Info.SessionNumber)
