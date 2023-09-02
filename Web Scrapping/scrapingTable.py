from csv import writer
import csv
import requests
import bs4
from pathlib import Path

res = requests.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
table_soup = soup.find_all('table')
filter_table = [table for table in table_soup if table.caption is not None]
# print(filter_table)
reqired_table = None

for table in filter_table:
    if str(table.caption.text).strip() == 'Top first languages by population per CIA[8]':
        reqired_table = table
        break

# print(reqired_table)
rows = reqired_table.find_all('tr')
# print(rows)
headers = [head.text.replace('\n', '') for head in rows[0].find_all('th')]
# print(headers)

data = []
for row_data in rows:
    value = row_data.find_all('td')
    value_text = [db.text.strip() for db in value]

    if len(value_text) == 0:
        continue

    data.append(value_text)

file = open(Path.home() / Path('OneDrive', 'Desktop', 'Wikipedia.csv'), 'w', newline='')
writer = csv.writer(file)
writer.writerow(headers)
writer.writerows(data)
file.close()
