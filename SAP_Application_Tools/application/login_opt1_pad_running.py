"""
This assumes the sap logon pad is already open and running (but not logged into active session).
obviously update sap "system" name and "windows_cred_name_search".
example below is using windows credentials manager for exmaple purposes only.
a stronger password manager would be more desired.
"""
import win32cred
import win32com.client

#uses windows credential manager
def get_sap_password(target="windows_cred_name_search"):
    cred = win32cred.CredRead(target, win32cred.CRED_TYPE_GENERIC)
    user = cred["UserName"]
    password = cred["CredentialBlob"].decode("utf-16-le").rstrip("\x00")
    return user, password
  
USER, PW = get_sap_password("windows_cred_name_search")  #name being searched must match the same as above

def get_session():
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    application = SapGuiAuto.GetScriptingEngine
    connection = application.OpenConnection("system", True) #update sap system name
    session = connection.Children(0)
    session_count = connection.Sessions.Count
    print(f"Connected sessions count: {session_count}")
    return session

def log_in(session):
    try:
        #this scripting language is pretty universal between companies and users
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = f"{USER}"
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = f"{PW}"
        session.findById("wnd[0]").sendVKey(0)
        print("logged into session.")
    except Exception as e:
        print("Failed to log into session.")

if __name__ == "__main__":
    session = get_session()
    log_in(session)
