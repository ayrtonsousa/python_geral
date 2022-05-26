import bs4

soup = bs4.BeautifulSoup(open('exemplo.html'))
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('algo inexistente') == None)
print(spanElem.attrs)