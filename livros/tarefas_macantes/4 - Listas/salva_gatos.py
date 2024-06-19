gatos = []

while True:
    nome = str(input("Escreve o nome do gato:"))

    gatos += [nome]

    for i in range(len(gatos)):
        print(f'Gato chamado {nome} adicionado')
        print(f'Total de gatos {len(gatos)}')