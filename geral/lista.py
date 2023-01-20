items = ['ola', 'tudo', 'bem']


# sem enumerate
# index = 0
# for i in items:
#     print(f'index:{index} item:{i}')
#     index += 1

# usando enumerate melhor
for index, i in enumerate(items):
    print(f'index:{index} item:{i}')


#zip para percorrer 2 listas juntas

precos = [0.99, 5.99, 20.50]
produtos = ['bala', 'bone', 'camiseta']

for preco, produto in zip(precos, produtos):
    print(f'preco:{preco} produto:{produto}')


# tira de map e reduce do python geral o inverter e concatenar com lista.py existente

lista = [1,2,3,4,5,6,7,8,9,10]

# posicao 
print(lista[0])

# ultimo lista
print(lista[-1])

# lista apenas os dois ultimos
print(lista[-2:])

# lista exceto os dois ultimos
print(lista[:-2])

# pular dois em dois
print(lista[::2])

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

