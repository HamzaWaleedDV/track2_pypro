import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scopes)
file = gspread.authorize(credentials)

#create new file
# new_file = file.create('new')
# new_file.share('hamzanasr412@gmail.com', perm_type='user', role='writer')

#open file
new_file = file.open('new')

# create new sheet
# worksheet = new_file.add_worksheet(title='Sheet2', rows = "100", cols= "20")

#write on the sheet
worksheet = new_file.worksheet("Sheet1")
worksheet.update('B1', 'Hamza')
worksheet.update_cell(2, 4, 'Hello!')

worksheet.update('A1:C2', [['Hadi', '1000', '2021-11-19'], ['Sara', '700', '2023-11-10']])
