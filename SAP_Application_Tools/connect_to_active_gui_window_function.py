"""
Function used to connect to active SAP GUI session, to begin writting automation workflows
"""

import win32com.client
import time

def get_sap_session():
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine

        if application.Connections.Count == 0:

        connection = application.Children(0)
        session = connection.Children(0)
        return session

    except Exception as e:
        print(f"Failed to attach to SAP session: {e}")
        return None
