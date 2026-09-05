"""
This is a common logoff procudure from the main/original session using the yellow logoff button, then handling the logoff confirmation popup messages.
The element ID for tbar[3, 15] might be different for your session, check the GUI scripting recorder if this isn't working.
"""

def logoff_original_session():
    try:
      for _ in range(5):
          try:
            session.findById("wnd[0]/tbar[3]/okcd").press()
            time.sleep(0.5)
            break
          except:
            pass
      session.findById("wnd[0]/tbar[15]/okcd").press()
      time.sleep(1.5)
    
      try:
          session.findById("wnd[0]/usr/btnSPOP-OPTION1").press()
      except:
          print(f"Error selecting logoff button popup: {e}")
    except Exception as e:
        print(f"logoff failed: {e}")
    
    try:
        session.findById("wnd[0]").close()
    except:
        pass
