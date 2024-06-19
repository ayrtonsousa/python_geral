from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumento1 = ExtratorArgumentosUrl(url)
argumento2 = ExtratorArgumentosUrl(url)

print(id(argumento1))
print(id(argumento2))
print(argumento1==argumento2)
print(argumento1)
moeda_origem, moeda_destino = argumento1.extrai_argumentos()
valor = argumento1.extrai_valor()