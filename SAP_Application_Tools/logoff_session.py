import win32com.client

def get_session()
  SapGuiAuto = win32com.client.GetObject("SAPGUI")
  application = SapGuiAuto.GetScriptingEngine
  connection = application.Children(0)
  session = connection.Children(0)
  session_count = connection.Sessions.Count
  print(f"Connected sessions count: {session_count}")
  return session

def log_off(session)
  try:
    session.findById("wnd[0]/tbar[0]/btn[15]").press()
    session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
  except Exception as e:
    print("Logoff failed with button option")
    print(e)

if __name__ == "__main__":
  session = get_session()
  log_off(session)
