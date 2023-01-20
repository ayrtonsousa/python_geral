
# usando o map
def multiplica_por_2(x):
    return x * 2

lista = [1,2,3,4,5]

print(list(map(multiplica_por_2, lista)))


# usando filter
def maior_que_zero(x):
    return x > 0

valores = [10, 4, -1, 3, 5, -9, -11]

print(list(filter(maior_que_zero, valores)))

# usando lambda ao inves de criar a funcao do ex. anterior
print(list(filter(lambda x: x > 0, valores)))


# usando reduce
# x e y são os primeiros valores da lista
# resultado da mult. se torna x e o y o proximo da sequencia, assim sucessivamente ate o fim
# retornando o resultado final de todas as multiplicacoes
from functools import reduce

minha_lista = [2, 4, 5, 2]

resultado_total = reduce(lambda x, y: x * y, minha_lista)
print(resultado_total)

# outro exemplo pegar maior valor
minha_lista2 = [2, 4, 5, 2, 3323, 2, 400, 6754, 77, 2000]
maior_valor = reduce(lambda x, y: x if (x > y) else y, minha_lista2)
print(maior_valor)