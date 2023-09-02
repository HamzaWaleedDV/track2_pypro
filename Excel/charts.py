import openpyxl
from pathlib import Path

excelFile = openpyxl.load_workbook(Path.home() / Path("OneDrive", "Desktop", "test.xlsx"))
sheet = excelFile['Sheet1']

#Charts
title = openpyxl.chart.Reference(sheet, min_col = 1, max_col = 1, min_row = 1, max_row = 6)
salary = openpyxl.chart.Reference(sheet, min_col = 2, max_col = 2, min_row = 1, max_row = 6)
#date = openpyxl.chart.Reference(sheet, min_col = 3, max_col = 3, min_row = 1, max_row = 6)
chart = openpyxl.chart.PieChart()

chart.title = 'My Chart'
chart.add_data(data = salary)
chart.set_categories(title)


sheet.add_chart(chart, 'E8')

#save
excelFile.save(Path.home() / Path("OneDrive", "Desktop", "test.xlsx"))