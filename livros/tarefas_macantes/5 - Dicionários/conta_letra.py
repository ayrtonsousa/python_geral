import pprint

mensagem = 'o rato roeu a roupa do rei de roma'
count = {}

for letra in mensagem:
    count.setdefault(letra,0)
    count[letra] = count[letra] + 1

pprint.pprint(count)