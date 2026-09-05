## 

## SAP GUI Automation Tools, Scripts, and Information regarding SAP (ECC, S4HANA, IBP, Fiori, Ondemand) application.

- A collection of Python scripts I've developed that automate SAP GUI workflows using the built-in scripting engine. These are mainly useful in environments where the official SAP APIs (like RFC or REST) are blocked or restricted by company policy.

## Why this exists

- A lot of companies disable or heavily restrict direct SAP API access for security, compliance, or licensing reasons. When that happens, you can't use libraries like pyrfc or the SAP Cloud SDK.
- This project takes a different approach: it attaches directly to an already running SAP GUI session. As long as you have an active SAP GUI session, these scripts can control it, open transactions, click buttons, navigate trees, create new sessions, etc. It's not as clean as a proper API, but it works when nothing else is allowed.

## How it works

The scripts uses win32com.client to talk to SAP GUI's built-in scripting interface. Once attached to a session, you can interact with it almost like a real user would.
The main pieces included are:

- get_sap_session() | Connects to an active SAP GUI window (handles the most common case of one connection).
- Multi-session helpers | Create additional sessions and minimize windows (useful when you need multiple sessions running in the background).
- SAP only allows for a maximum of 5 open active sessions per system.
  - When combining multiple workflows working alongside eachother. I've found the best practice is to call SAP transactions by the exact t-code name, rather than the system name it gives you when you record the scripts steps using the SAP GUI scripting recorder.
  - Most transaction T-codes have standard names, that are used in every SAP system no matter the company. If a company has custom T-Codes, they usually start with "Z" or "ZTC".

## Requirements

- Windows machine (SAP GUI scripting only works on Windows)
- SAP GUI installed and running
- SAP GUI scripting enabled for your user (sometimes requires a Basis admin to allow it)
- Python 3.x with `pywin32` installed

```bash
pip install pywin32
```

## Basic Usage For Interacting With SAP GUI Session

```python

from sap_gui_utils import get_sap_session

session = get_sap_session()

if session:
    #Example: maximize the main window
    session.findById("wnd[0]").maximize()
    
    #Do whatever you need...
else:
    print("No active SAP session found. Please log in first.")

```

## Important Notes

- This method is more fragile than a real API. Screen changes, popups, or SAP upgrades can break things.
- It only works while SAP GUI is open and you're logged in.
- Don't run this on a machine where someone else might be actively using the same SAP session.
- Use it responsibly. It's meant for legitimate automation when official APIs aren't available.

## Disclaimer

This is a workaround for environments where proper SAP integration is blocked. If your company ever opens up API access, you should probably switch to that instead.

