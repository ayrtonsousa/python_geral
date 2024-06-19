#! python

# Abre varios resultados de pesquisa no google
# python google_sorte.py termo_da_pesquisa

import requests, sys, webbrowser, bs4

print('Googlando...') #Imprime enquanto realiza a busca
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
print(res.raise_for_status())

#Obtém os links dos principais resultados da pesquisa
soup = bs4.BeautifulSoup(res.text)

#Abre uma aba no navegador para cada resultado
linkElems = soup.select('.r a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))