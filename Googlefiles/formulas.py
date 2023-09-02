import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scopes)
file = gspread.authorize(credentials)

new_file = file.open("example")
worksheet = new_file.worksheet("Sheet1")

worksheet.update_cell(8, 2, "=SUM(B2:B7)")
worksheet.update_cell(9, 2, "=MAX(B2:B7)")
worksheet.update_cell(10, 2, "=AVERAGE(B2:B7)")

cell = worksheet.acell('B8', value_render_option='FORMULA').value
print(cell)