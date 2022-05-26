
lista = [15, 87, 32, 65, 56, 32, 49, 37]


lista_ordena_crescente = sorted(lista)
print(lista_ordena_crescente)

lista_ordem_decrescente = sorted(lista, reverse=True)
print(lista_ordem_decrescente)

lista_ordenacao_reversa = reversed(lista)
print(list(lista_ordenacao_reversa))

lista.sort()
lista.sort(reverse=True)
print(lista)