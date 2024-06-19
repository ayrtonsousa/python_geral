import requests,bs4

#pagina web
res = requests.get('https://nostarch.com/')
print(res.raise_for_status())
noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))

#pagina local
exampleFile = open('exemplo.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))