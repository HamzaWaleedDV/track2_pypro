import sqlite3
from pathlib import Path

sqliteConnection = sqlite3.connect(Path.home() / Path('OneDrive', 'Desktop', 'DataBase.db'))
crsr = sqliteConnection.cursor()
print('Connected to the database')

crsr.execute("SELECT Name,Salary,dateOfEmployement FROM employees where salary > 850")
# print(crsr.fetchall())
# print(crsr.fetchone())
# print(crsr.fetchmany(3))

answer = crsr.fetchall()

for i in answer:
    print(i)