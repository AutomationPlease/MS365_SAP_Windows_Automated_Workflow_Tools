## Tools and Information regarding SAP (ECC, S4HANA, IBP, Fiori, Ondemand) application.



## Common SAP scripting interactions

| Action                      | Command                                    |          
|-----------------------------|--------------------------------------------|
| `minimize SAP window`       | session.findByID("wnd[0]").iconify()       |
| `create new SAP session`    | session.createSession()                    |
| `close SAP session`         | session.findById("wnd[0]").close()         |
| `maximize SAP window`       | session.findById("wnd[0]").maximize()      |
