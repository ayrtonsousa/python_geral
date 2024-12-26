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

list_dict = [
    {"id": 8, "name": "ayrton"},
    {"id": 9, "name": "ayrtony"},
    {"id": 3, "name": "byrtonb"},
    {"id": 5, "name": "cyrtond"},
    {"id": 6, "name": "fyrtonf"},
    {"id": 7, "name": "zyrtonh"},
    {"id": 1, "name": "yrtonj"},
    {"id": 2, "name": "hayrton"},
]

list_dict = sorted(list_dict, key=lambda d: d['name']) 

print(list_dict)


fruits = ['grape', 'Raspberry', 'apple', 'Banana']
print(sorted(fruits, key=len, reverse=True)) #ordem do maior pro menor
print(sorted(fruits, key=str.lower)) #ordem do menor pro maior ignorando o uppercase
