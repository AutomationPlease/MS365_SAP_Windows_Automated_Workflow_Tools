## Common SAP scripting interactions

| Action                             | Command                                                          |          
|------------------------------------|------------------------------------------------------------------|
| `minimize SAP window`              | session.findByID("wnd[0]").iconify()                             |
| `create new SAP session`           | session.createSession()                                          |
| `close SAP session`                | session.findById("wnd[0]").close()                               |
| `maximize SAP window`              | session.findById("wnd[0]").maximize()                            |
| `execute button press`             | session.findById("wnd[0]/tbar[0]/btn[0]").press()                |
| `Tcode Search Box (input)`         | session.findById("wnd[0]/tbar[0]/okcd").text = "Tcode-Name"      |
| `yellow logoff/exit button (back)` | session.findById("wnd[0]/tbar[0]/btn[15]").press()               |
| `pop up window button selection, 1`| session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()           |
| `pop up window button selection, 2`| session.findById("wnd[1]/usr/btnSPOP-OPTION2").press()           |
