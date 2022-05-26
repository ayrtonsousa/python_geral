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