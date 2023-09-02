import openpyxl
from pathlib import Path

excelFile = openpyxl.load_workbook(Path.home() / Path("OneDrive", "Desktop", "test.xlsx"))
sheet = excelFile['Sheet1']

sheet['B7'] = '=SUM(B1:B6)'
sheet['B8'] = '=average(B1:B6)'
sheet['B9'] = '=COUNTIF(B1:B6, ">750")'

excelFile.save(filename=Path.home() / Path("OneDrive", "Desktop", "test.xlsx"))