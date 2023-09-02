import csv
from pathlib import Path

# file = open(Path.home() / Path('OneDrive', 'Desktop', 'CSV files', 'employees_1.csv'), 'a', newline='')
# dictWriter = csv.DictWriter(file, ['Name', 'Salary', 'Date'], delimiter=';')
# dictWriter.writerow({'Name': 'Ali', 'Salary': 1500, 'Date':'09/07/2023'})
# file.close()

file = open(Path.home() / Path('OneDrive', 'Desktop', 'employees_test.csv'), 'w', newline='')
