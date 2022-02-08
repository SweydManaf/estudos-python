import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")

# elems = exampleSoup.select('#author')
# print(elems[0].getText())

# Obtendo dados dos atributos

spanElem = exampleSoup.select('span')[0]
idOfSpan = spanElem.attrs
print(idOfSpan)