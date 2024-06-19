lista = [23, 35, 7, 76, 45, 13]

for i in range(len(lista)):
    print(i, lista[i])

print(list(range(len(lista))))

print(list(enumerate(lista)))

for indice, valor in enumerate(lista):
    print(indice, valor)

usuarios = [
    ("Ayrton", 26, 1995),
    ("Cleiton", 27, 1994),
    ("Ariston", 31, 1990),
]

for nome, idade, ano in usuarios:
    print(nome, idade, ano)

for _, idade, _ in usuarios:
    print(idade)