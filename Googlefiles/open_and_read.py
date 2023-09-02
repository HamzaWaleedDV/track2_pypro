import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scopes)
file = gspread.authorize(credentials)
# sheet = file.open('example')
sheet = file.open_by_url("https://docs.google.com/spreadsheets/d/1UYPL-GdPSr0ctFhaWOn_kRlcJlhJTzcxK6QGMmS4VUc/edit?usp=drive_link")

# worksheet = sheet.get_worksheet(0)
worksheet = sheet.worksheet('Sheet1')
worksheet_list = sheet.worksheets()
print(worksheet_list)

val = worksheet.acell('B1').value
print(val)

val = worksheet.acell('A5').value
print(val)

val = worksheet.cell(5, 1).value
print(val)

val = worksheet.row_values(2)
print(val)

val = worksheet.col_values(1)
print(val)

val = worksheet.get_all_values()
print(val)

val = worksheet.get_all_records()
print(val)