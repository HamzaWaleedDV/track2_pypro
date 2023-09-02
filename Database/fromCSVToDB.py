import sqlite3
import csv
from pathlib import Path

sqliteConnection = sqlite3.connect(Path.home() / Path('OneDrive', 'Desktop', 'DataBase.db'))
crsr = sqliteConnection.cursor()
print('Connected to the database')

#Create Table
sql_command = """CREATE TABLE if not exists employees (
id INTEGER,
Name VARCHAR(20),
Salary INTEGER,
dateOfEmployement TEXT)"""

crsr.execute(sql_command)

#read File
file = open(Path.home() / Path('OneDrive', 'Desktop', 'employees_1.csv'))
rows = csv.reader(file)

#add data
crsr.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", rows)


sqliteConnection.commit()
sqliteConnection.close()