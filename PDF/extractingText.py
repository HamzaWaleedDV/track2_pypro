import PyPDF2
from pathlib import Path

pdfFile = open(Path.home() / Path('OneDrive', 'Desktop', 'pdf_test.pdf'), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

#pages number
print(pdfReader.numPages)

#read
page = pdfReader.getPage(1)
print(page.extractText())

pdfFile.close()