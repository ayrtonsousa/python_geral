import requests

#Salva dados da pagina web

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.raise_for_status())

playFile = open('RomeuEJulieta.txt','wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)

playFile.close()