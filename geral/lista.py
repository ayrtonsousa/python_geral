items = ['ola', 'tudo', 'bem']

# sem enumerate
# index = 0
# for i in items:
#     print(f'index:{index} item:{i}')
#     index += 1

# usando enumerate melhor
for index, i in enumerate(items):
    print(f'index:{index} item:{i}')


# usando range para tabuada
def tabuada(x):
    for i in range(1, 11):
        print(f"{x} x {i}: {x * i}")

tabuada(9)


#zip para percorrer 2 listas juntas

precos = [0.99, 5.99, 20.50]
produtos = ['bala', 'bone', 'camiseta']

for preco, produto in zip(precos, produtos):
    print(f'preco:{preco} produto:{produto}')

lista = [1,2,3,4,5,6,7,8,9,10]

# posicao 
print(lista[0])

# ultimo lista
print(lista[-1])

# comeca na posicao x
print(lista[3:])

# vai ate posicao x
print(lista[:3])

# lista exceto os dois ultimos
print(lista[:-2])

# lista apenas os dois ultimos
print(lista[-2:])

# pular dois em dois
print(lista[::2])

# pular dois em dois, invertido
print(lista[::-2])

# posicao 1 ao 4 pulando em 2 
print(lista[1:4:2])

# pular dois em dois depois do 1
print(lista[1::2])

# matriz
listas = [[1,2,3],[4,5,6],[7,8,9]]

# invertendo uma linha da matriz
print(listas[2][::-1])

lista = [1,2,3,4,5]
# adicionar ao fim
lista.append(6)
print(lista)

# adicionar no começo
lista.insert(0, 999)
print(lista)

# remover do comeco e retorna valor
print(lista.pop(0))

# remover do fim e retorna valor
print(lista.pop(-1))

# Remove primeira ocorrencia de valor 3
lista.remove(3)
print(lista)

# reverte sequencia
lista.reverse()
print(lista)

# reverte mas sem modifica lista
print(list(reversed(lista)))


# inverter ordem string, lista, etc ...
string1 = 'Olá mundo'
print(string1[::-1])

# aparicoes na lista do numero 3
lista = [1,1,2,3,3,3,3,4]
print(lista.count(3))


# ordenar por idade
nomes = [
    {'nome': 'luciano', 'idade': 29},
    {'nome': 'calleri', 'idade': 31},
    {'nome': 'james', 'idade': 32},
    {'nome': 'ferreira', 'idade': 26},
    {'nome': 'williams gomes', 'idade': 20},
]

nomes.sort(key=lambda item:item['idade'])
print(nomes)

# ordernar lista com dicionario por data
from datetime import datetime

partidas = [
    {'data':'2024-01-01','rival':'palmeiras'},
    {'data':'2024-01-07','rival':'ldu'},
    {'data':'2024-01-03','rival':'corinthians'},
    {'data':'2023-06-05','rival':'criciuma'},
    {'data':'2023-03-01','rival':'coritiba'},
    {'data':'2023-12-31','rival':'santos'},
    {'data':'2023-11-01','rival':'cuiaba'}
]

partidas.sort(key=lambda item: datetime.strptime(item['data'], "%Y-%m-%d"))

print(partidas)

# ordenando uma lista dentro de outra 
times = [
    {'time':'spfc','partidas':['2025-03-30','2025-02-01','2025-12-05','2025-06-07']},
    {'time':'palmeiras','partidas':['2025-03-23','2025-05-07','2025-11-10','2025-08-09']},
    {'time':'santos','partidas':['2025-01-13','2025-01-30','2025-07-25','2025-02-20']},
    {'time':'corinthians','partidas':['2025-12-30','2025-05-02','2025-11-26','2024-09-07']},
]

# precisa usar list depois do map
list(map(lambda time: time['partidas'].sort(key=lambda x: datetime.strptime(x, '%Y-%m-%d')), times))

print(times)
