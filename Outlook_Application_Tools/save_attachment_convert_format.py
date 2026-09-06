import os
import win32com.client as win32
from datetime import datetime

SAVE_DIR = r"X:\Folder Name\Sub Folder Namer"  #save path for attachment
OUTLOOK_FOLDER = "Target_Outlook_Folder"  #outlook target folder name 
timestamp_datasource = datetime.now().strftime("%m.%d.%Y")  #add date stamp (and time if needed) to make file saves unique so no future overwrites when this runs continually.
attachment_xlsx = os.path.join(SAVE_DIR, f"Excel_DataSource_{timestamp_datasource}.xlsx") #attachment rename

#function for targeting outlook folder
def get_target_folder(namespace):
    inbox = namespace.GetDefaultFolder(6)
    try:
        return inbox.Folders[OUTLOOK_FOLDER]
    except Exception:
        return namespace.Folders.Item(1).Folders[OUTLOOK_FOLDER]

#you must have a running outlook session open or minimized
outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
folder = get_target_folder(outlook)

#grab only the newest file from the folder
msg = messages.GetFirst()
messages = folder.Items
messages.Sort("[ReceivedTime]", True)
if msg is None:
    raise RuntimeError(f"No mail in Outlook folder {OUTLOOK_FOLDER}")

#can remove print after confirmation of successful run. I was using this mainly for testing targeting other folders or other emails.
print("Using mail:", msg.Subject, ," | ", msg.ReceivedTime)

#alot of times the attachment (in this case excel) is in a format that I need converted to xlsx. Most of the time it's binary format I need to change since Python doesn't work well with it.
saved_xlsb = None
for att in msg.Attachments:
    name = att.FileName
    if name.lower().endswith((".xlsb")):
        saved_xlsb = os.path.join(SAVE_DIR, name)
        att.SaveAsFile(saved_xlsb)
        print("Saved attachment:", saved_xlsb)
        break

if not saved_xlsb:
    raise RuntimeError("Newest mail has no Excel attachment.")

#turn off excel visual updates, open the binary excel file, convert to xlsx, save, quit excel.
excel = win32.DispatchEx("Excel.Application")
excel.Visible = False
excel.DisplayAlerts = False
try:
    wb = excel.Workbooks.Open(saved_xlsb)
    if os.path.exists(attachment_xlsx):
        os.remove(attachment_xlsx)
    wb.SaveAs(attachment_xlsx, FileFormat=51)  #.xlsx
    wb.Close(SaveChanges=False)
finally:
    excel.Quit()
    print("Converted and saved file:", attachment_xlsx)
