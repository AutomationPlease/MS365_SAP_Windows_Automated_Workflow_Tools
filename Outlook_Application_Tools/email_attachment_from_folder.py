"""if you use multiple emails that are connected via user profile settings in outlook then you can send emails from the
active user session through the designated user profile of your choice without using send on behalf which is blocked by most companies.
as long as you can go to file -> change user profile -> select multiple user profiles, and you have the accounts setup/connected,
then you can send emails through any of those user profile addresses."""

import os
import win32com.client as win32
from datetime import datetime

FOLDER = r"X:\Folder Name\Sub Folder Namer"  #target folder file is stored
timestamp = datetime.now().strftime("%m.%d.%Y")
report = os.path.join(FOLDER, f"Excel_DataSource_{timestamp_datasource}.xlsx")  #target file from folder

TO = [
    "email",
]

CC = [
    "email"
]

SUBJECT = f"Email Subject {timestamp}"
BODY = f"""Email body.
"""

if not os.path.exists(report):
    raise FileNotFoundError(f"File not found: {report}")

#email from secondary outlook user profile connected to main user profile active session (no need to switch accounts to send email). Change 'sending email' to the email you'd want the message sent from.
outlook = win32.Dispatch("Outlook.Application")
sendingemail = None
#loop through user profile options until you match with a user profile for sendingemail@...
for i in range(1, outlook.Session.Accounts.Count +1):
    acct = outlook.Session.Accounts.Item(i)
    blob = f"{acct.DisplayName} {getattr(acct, 'smtpAddress', '')}".lower()
    print("Account:", acct.DisplayName, getattr(acct, "SmtpAddress", ""))
    if "sendingemail@" in blob:
        sendingemail = acct
        break
if sendingemail is None:
    raise RuntimeError("Sending email is not in this Outlook profile.")

inbox = sendingemail.DeliveryStore.GetDefaultFolder(6)
mail = inbox.Items.Add("IPM.Note")
mail.SendUsingAccount = sendingemail
mail.To = "; ".join(TO)
mail.CC = "; ".join(CC)
mail.Subject = SUBJECT
mail.Body = BODY
mail.Attachments.Add(report)

mail.Send()
# mail.Display() #opens draft and doesnt send (can show you who sender is)

print("Emailed:", report)
