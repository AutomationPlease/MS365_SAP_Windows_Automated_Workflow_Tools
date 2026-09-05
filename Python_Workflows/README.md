## Automation Tools

Small collection of scripts I use to keep a Windows machine awake and simulate light user activity during long-running jobs. Built mainly for data work where processes can take hours and I don’t want the machine to sleep or lock in the middle of a run.

## What’s in here

| File                        | Purpose                                              | Notes                              |
|-----------------------------|------------------------------------------------------|------------------------------------|
| `keep_alive.pyw`            | Prevents sleep + small mouse movements               | No external dependencies           |
| `smart_mouse_clicker.pyw`   | Moves mouse to a blank area on screen and clicks     | Uses absolute coordinates          |
| `start_automation.bat`      | Starts both scripts in the right order               | Easy one-click launcher            |

## Quick start

1. Clone or download the folder
2. Create a virtual environment (recommended):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Double-click start_automation.bat

- The batch file starts keep_alive.pyw first, waits a couple seconds, then starts smart_mouse_clicker.pyw.
- Both run in the background using pythonw.exe (no console windows).

## Adding more scripts
If you want to add other automation scripts later, just add them in the batch file after keep_alive.pyw.

Example:

```batch
@echo off

cd /d "%~dp0"

start "" ".venv\Scripts\pythonw.exe" "keep_alive.pyw"

timeout /t 2 >nul

:: Add new tools below this line

start "" ".venv\Scripts\pythonw.exe" "new_script.pyw"
```

Keeping keep_alive first matters because it sets the Windows execution state that tells the system “I’m still in use.”. Starting it early gives the other scripts a more stable environment.

## Logging
Both scripts write to log files in the same folder:

- keep_alive.log
- mouse_clicker.log

These are plain text and append-only, so you can check them anytime to see what’s been happening.

## A few notes

- These tools work well for most personal and light corporate use cases. However, many company environments have aggressive Group Policy or Intune settings that will still lock the machine after a certain time or overnight regardless of activity. These scripts can delay that, but they can’t always override strict policies.
- The mouse clicker uses absolute screen coordinates so it can target the lower-right area of the desktop (usually empty). If you’re running it while another application is maximized, it may click inside that window instead.
- The smart_mouse_clicker.pyw currently has an input() line at the end. If you want it to run completely silently with pythonw.exe, you can remove that line.

## Why I made this

- I work with data pipelines and automation that sometimes run for a long time. Rather than constantly adjusting power settings or baby-sitting the machine, I wanted something simple and reliable that just works in the background. These scripts are the result.
- Feel free to use them, tweak them, or add your own tools to the batch file.
