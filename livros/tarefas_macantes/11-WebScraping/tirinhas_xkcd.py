#! python
# downloadXkcd.py - Download das tirinhas do site

import requests, os, bs4

url = 'https://xkcd.com' # url
os.makedirs('xkcd', exist_ok=True) # armazena tiras em ./xkcd
while not url.endswith('#'):
    
    # Download da pagina
    print('Downloading da página %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Encontra url da tirinha
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Não pode encontrar tirinha')
    else:
        comicUrl = comicElem[0].get('src')
        comicUrl = 'https:'+comicUrl #Inclui https para baixar imagem

        # Download da imagem
        print('Download da imagem %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Salva a imagem em ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Pega o url do botao prev
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Feito')
