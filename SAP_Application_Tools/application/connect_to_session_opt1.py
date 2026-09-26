"""
function for connecting to active sap session for scripting purposes.
"""

import win32com.client

def get_session():
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    application = SapGuiAuto.GetScriptingEngine
    connection = application.Children(0)
    session = connection.Children(0)
    session_count = connection.Sessions.Count
    print(f"Connected sessions count: {session_count}")
    return session

if __name__ == "__main__":
    session = get_session()
