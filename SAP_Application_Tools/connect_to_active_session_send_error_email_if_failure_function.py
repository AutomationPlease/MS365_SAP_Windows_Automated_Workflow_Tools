"""
Connect to active SAP GUI session function.
Send connection error email via outlook if failed.
"""

import win32com.client as win32, win32com
from datetime import datetime

timestamp = datetime.now().strftime("%m/%d/%Y | %H:%M:%S")

def get_sap_session():
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.Children(0)
        original_session = connection.Children(0)
    except Exception as e:
        print(f"Failed to attach to SAP session: {e}")
        try:
            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreatItem(0)
            mail.To = "add email to send connection fail direct message to."
            mail.Subject = f"Error: SAP GUI Connection Error {timestamp}"
            mail.Body = f"SAP GUI Connection Failed: \n{str(e)}"
            mail.Send()
        except:
            pass
        exit()
