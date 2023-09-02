import sqlite3
from pathlib import Path
import openpyxl

sqliteConnection = sqlite3.connect(Path.home() / Path('OneDrive', 'Desktop', 'DataBase.db'))
crsr = sqliteConnection.cursor()
print('Connected to the database')

crsr.execute("SELECT firstName,lastName,age FROM students")

info = crsr.fetchall()

file = openpyxl.Workbook()
file.active.title = "Information"
sheet = file.active

for i, row in enumerate(info):
    for j, value in enumerate(row):
        sheet.cell(row=i+1, column=j+1).value = value


file.save(Path.home() / Path('OneDrive', 'Desktop', 'Students1.xlsx'))        