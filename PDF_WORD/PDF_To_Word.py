from pdf2docx import Converter
from pathlib import Path

pdf_file = Path.home() / Path('OneDrive', 'Desktop', 'article', 'article.pdf')
docx_file =  Path.home() / Path('OneDrive', 'Desktop', 'article.docx')

#convert
cv = Converter(pdf_file)
# cv.convert(docx_file)
cv.convert(docx_file, start=1, end=3)
cv.close()