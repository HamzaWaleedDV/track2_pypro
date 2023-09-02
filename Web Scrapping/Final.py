from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from pathlib import Path

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')

tables = browser.find_elements(By.TAG_NAME, 'table')
required_table = None

caption = browser.find_elements(By.TAG_NAME, 'caption')


for number, table in enumerate(tables):
    if caption[number].text.strip() == 'Top first languages by population per CIA[8]':
        required_table = table
        break


headers = required_table.find_elements(By.TAG_NAME, 'th')

rows = required_table.find_elements(By.TAG_NAME, 'td')

#create Excel File
file = openpyxl.Workbook()
activeSheet = file.active
activeSheet.title = 'Table'

sheet = file['Table']

row_index = 0
cell_index = 0

# تعيين قيم العناوين في الخلايا
for i, header in enumerate(headers):
    sheet[chr(65 + cell_index) + str(row_index + 1)] = header.text
    cell_index = (cell_index + 1) % 3
    if cell_index == 0:
        row_index += 1

# تعيين قيم الصفوف في الخلايا
for i, row in enumerate(rows):
    sheet[chr(65 + cell_index) + str(row_index + 1)] = row.text
    cell_index = (cell_index + 1) % 3
    if cell_index == 0:
        row_index += 1

file.save(Path.home() / Path('OneDrive', 'Desktop', 'Table.xlsx'))