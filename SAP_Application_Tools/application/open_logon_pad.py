"""
launch sap launch pad for selecting correct system to log in to.
"""

import win32com.client
import time
import subprocess

#sap exe usually lives in program files
SAP_LOGON_PATH = r"C:\Program Files\SAP\FrontEnd\SAPgui\saplogon.exe" 
SAP_SYSTEM_NAME = "System"

def open_logon_pad():
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
    except Exception:
        subprocess.Popen([SAP_LOGON_PATH])
        SapGuiAuto = None
        for _ in range(20):
            time.sleep(1)
            try:
                SapGuiAuto = win32com.client.GetObject("SAPGUI")
                break
            except Exception:
                pass
        if SapGuiAuto is None:
            raise RuntimeError("SAP Logon pad did not start")
    application = SapGuiAuto.GetScriptingEngine
    return application

if __name__ == "__main__":
    open_logon_pad()
