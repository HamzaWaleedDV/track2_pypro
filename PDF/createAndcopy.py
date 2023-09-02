from PyPDF2 import PdfFileWriter as w
from pathlib import Path
import PyPDF2

#create
pdf = w()
file = open(Path.home() / Path('OneDrive', 'Desktop', 'pdf_file.pdf'), 'wb')
for i in range(5):
    pdf.addBlankPage(219,297)

pdf.write(file)    

#copy and paste
pdfFile = open(Path.home() / Path('OneDrive', 'Desktop', 'pdf_test.pdf'), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

for pageNum in range(pdfReader.numPages):
    page = pdfReader.getPage(pageNum)
    pdf.addPage(page)

pdf.write(file)
file.close()