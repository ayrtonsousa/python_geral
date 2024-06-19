# 2.5
symbols = '$¢£¥€¤'

print(tuple(ord(symbol) for symbol in symbols))

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

# 2.6 diferente da 2.4 nao e criada em memoria, usando genexp evitaria o custo
# de um exemplo de 2 listas com mil itens virar 1 milhão somente pra alimentar o laço for
# assim criando um de cada vez, nao gerando uma lista que consumiria memoria

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

