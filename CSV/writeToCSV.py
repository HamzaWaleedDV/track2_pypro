import csv
from pathlib import Path

# header = [
#     'Name',
#     'Salary',
#     'Date'
# ]

# data = [
#     ['Hadi', 1000, '04/08/2021'],
#     ['Sara', 800, '06/04/2021'],
#     ['Reem', 400, '25/02/2020'],
#     ['Yara', 750, '09/07/2020'],
#     ['Anas', 1200, '15/04/2019'],
# ]

# file = open(Path.home() / Path('OneDrive', 'Desktop', 'CSV files', 'employees_1.csv'), 'w', newline='')
# writer = csv.writer(file)
# writer.writerow(header)
# writer.writerows(data)
# file.close()

file = open(Path.home() / Path('OneDrive', 'Desktop', 'CSV files', 'employees_1.csv'), 'w', newline='')
writer = csv.writer(file, delimiter='\t', lineterminator='\n-----------------------------\n')
writer.writerow(['Hadi', 1000, '04/08/2021'])
writer.writerow(['Anas', 100, '04/08/2021'])
writer.writerow(['Sara', 500, '04/08/2021'])
file.close()