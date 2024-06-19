"""
Se os números de 1 a 5 fossem escritos em palavras: um, dois, três, quatro, cinco, então teríamos utilizado 2 + 4 + 4 + 6 + 5 = 21 letras no total.

Se todos os números de 1 até 1000 fossem escritos em palavras, quantas letras nós teríamos utilizado?
"""

numeros = {
    1:'um',
    2:'dois',
    3:'tres',
    4:'quatro',
    5:'cinco',
    6:'seis',
    7:'sete',
    8:'oito',
    9:'nove'
}

inicio = 1
fim = 1000

total = 0
for sequencia in range(inicio,fim+1):
    for palavra in str(sequencia):
        numero = int(palavra)
        if numero > 0:
            total += len(numeros[numero])

print(total)