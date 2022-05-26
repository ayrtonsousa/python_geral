import bs4

#buscando pelo id
exampleFile = open('exemplo.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(elems[0])
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

#buscando pela tag
pElems = exampleSoup.select('p')
print(pElems[0])
print(pElems[0].getText())
print(pElems[1])
print(pElems[1].getText())
print(str(pElems[2]))
