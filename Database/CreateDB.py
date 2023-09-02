import sqlite3
from pathlib import Path

sqliteConnection = sqlite3.connect(Path.home() / Path('OneDrive', 'Desktop', 'DataBase.db'))
crsr = sqliteConnection.cursor()
print('Connected to the database')


sql_Command = """CREATE TABLE if not exists students (
firstName VARCHAR(20),
lastName VARCHAR(20),
age INTEGER)"""

crsr.execute(sql_Command)

#INSERT data
crsr.execute('INSERT INTO students VALUES ("Hadi", "Hasan", 23);')
crsr.execute('INSERT INTO students VALUES ("Yara", "Anas", 26);')
crsr.execute('INSERT INTO students VALUES ("Sara", "Hasan", 30);')

sqliteConnection.commit()

#cls connection
sqliteConnection.close()