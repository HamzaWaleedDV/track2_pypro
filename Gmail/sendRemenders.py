# import openpyxl, smtplib
# from pathlib import Path


# file = openpyxl.load_workbook(Path.home() / Path("OneDrive", "Desktop", "members.xlsx"))

# sheets = file.sheetnames
# sheet = file['Sheet1']
# lastCol = sheet.max_column
# latestMonth = sheet.cell(row=1, column=lastCol).value
# # print(latestMonth)

# unpaidMembers = {}

# for r in range(2, sheet.max_row + 1):
#     payment = sheet.cell(row=r, column=lastCol).value
#     if payment != 'paid':
#         name = sheet.cell(row=r, column=1).value
#         email = sheet.cell(row=r, column=2).value
#         unpaidMembers[name] = email

# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.starttls()
# sender_email = 'hamzanasr412@gmail.com'
# password = input(str("Please Enter your password: "))
# smtpObj.login(sender_email, password)

# for name, email in unpaidMembers.items():
#     body = """Subject: %s does unpaid.\nDear %s,\nRecords show that you have not paid does 
#     for %s.\nPlease make this payment as soon possible.\nThank you.""" %(latestMonth, name, latestMonth)
#     print('Sending email to %s' % email)
#     sendmailStatus = smtpObj.sendmail(sender_email, email, body)

#     if sendmailStatus != {}:
#         print("There was a proplem sendingg email to %s: %s" %(email, sendmailStatus))

# smtpObj.quit()


list1 = [1, 3, 5]
list2 = [1, 2, 4]

list3 = sorted(list1 + list2)
print(list3)