import bs4
from pathlib import Path

exampleFile = open(Path.home() / Path('OneDrive', 'Desktop', 'example.html'))
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')

element = exampleSoup.select('p')
print(element)
print(len(element))
print(element[0].getText())
print(element[0].attrs)
print(element[1].attrs)