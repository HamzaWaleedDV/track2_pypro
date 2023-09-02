import csv, os
from pathlib import Path

os.makedirs(Path.home() / Path('OneDrive', 'Desktop', 'CSV files'), exist_ok=True)

for csvFileName in os.listdir(Path.home() / Path('OneDrive', 'Desktop', 'CSV files')):
    if not csvFileName.endswith('.csv'):
        continue

    print('Removing header from ', csvFileName, '........')
    csvRows = []
    csvFileObj = open(Path.home() / Path('OneDrive', 'Desktop', 'CSV files', csvFileName))
    readerObj = csv.reader(csvFileObj)

    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()  

    csvFileObj = open(Path.home() / Path('OneDrive', 'Desktop', 'CSV files', csvFileName), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()    
