"""Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos

Exemplo:

Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150

Saída: [100-105], [110-111], [113-115], [150]"""

numeros = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150, 152, 153]

intervalos = ''
intervalo = []

for numero in numeros:
    if intervalo == []:
        intervalo.append(numero)
    else:
        diferenca = numero - intervalo[-1] 
        if diferenca == 1:
            intervalo.append(numero)
        else:
            primeiro = str(intervalo[0])
            ultimo = str(intervalo[-1])
            if len(intervalo) == 1:
                intervalos += '[' + ultimo + ']'
            else:
                intervalos += '[' + primeiro + '-' + ultimo + ']'
            intervalo = [numero]

if len(intervalo) == 1:
    intervalos += '[' + str(numeros[-1]) +']'
else:
    intervalos += '[' + str(intervalo[0]) + '-' + str(intervalo[-1]) +']'

print(intervalos)