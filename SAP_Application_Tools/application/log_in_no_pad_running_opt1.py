"""
This assumes the sap logon pad is not open and running.
obviously update sap "system" name and "windows_cred_name_search".
example below is using windows credentials manager for example purposes only.
a stronger password manager would be more desired.
"""
import win32cred
import win32com.client
import time
import subprocess

#uses windows credential manager
def get_sap_password(target="windows_cred_name_search"):
    cred = win32cred.CredRead(target, win32cred.CRED_TYPE_GENERIC)
    user = cred["UserName"]
    password = cred["CredentialBlob"].decode("utf-16-le").rstrip("\x00")
    return user, password

USER, PW = get_sap_password("windows_cred_name_search")  #name being searched must match the same as above
SAP_LOGON_PATH = r"C:\Program Files\SAP\FrontEnd\SAPgui\saplogon.exe" #sap exe usually lives in program files
SAP_SYSTEM_NAME = "system"

def open_logon_pad():
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
    except Exception:
        subprocess.Popen([SAP_LOGON_PATH])
        SapGuiAuto = None
        for _ in range(20):
            time.sleep(5) #usually takes ~5 seconds for logon pad to open
            try:
                SapGuiAuto = win32com.client.GetObject("SAPGUI")
                break
            except Exception:
                pass
        if SapGuiAuto is None:
            raise RuntimeError("SAP Logon pad did not start")
    application = SapGuiAuto.GetScriptingEngine
    return application

def get_session():
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    application = SapGuiAuto.GetScriptingEngine
    connection = application.OpenConnection(f"{SAP_SYSTEM_NAME}", True)
    session = connection.Children(0)
    session_count = connection.Sessions.Count
    print(f"Connected sessions count: {session_count}")
    return session

def log_in(session):
    try:
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = f"{USER}"
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = f"{PW}"
        session.findById("wnd[0]").sendVKey(0)
        print("logged into session.")
    except Exception as e:
        print("Failed to log into session.")

if __name__ == "__main__":
    open_logon_pad()
    session = get_session()
    log_in(session)
