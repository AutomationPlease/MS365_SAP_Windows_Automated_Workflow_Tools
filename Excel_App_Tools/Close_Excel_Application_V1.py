# option for closing excel window

import win32com.client

excel = win32com.client.GetObject(Class="Excel.Application")
for wb in excel.Workbooks:
    print("OPEN:", wb.Name)
for wb in list(excel.Workbooks):
    if f"excel file name you are trying to close" in wb.Name.lower():
        wb.Saved = True
        wb.Close(SaveChanges=False)
if excel.Workbooks.Count == 0:
    excel.Quit()
