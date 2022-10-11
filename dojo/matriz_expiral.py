""" Dado um número de colunas e um número de linhas, retornar uma matriz em espiral de fora para dentro no sentido horário. 

Entrada: 5 6

Saída:
 1  2  3  4  5
18 19 20 21  6
17 28 29 22  7
16 27 30 23  8
15 26 25 24  9
14 13 12 11 10

"""

colunas = int(input("Colunas:\n"))
linhas = int(input("Linhas:\n"))

# cria dicionario para mapear
posicoes = {str(i): 0 for i in range(1, (colunas * linhas) + 1)}

colunas_exp = colunas
linhas_exp = linhas
posicao = 0
passo = 1
x = 0

# cria posicoes
for key in posicoes.keys():
    em_validacao = True

    while em_validacao:

        # cima
        if passo == 1:
            if x < colunas_exp:
                posicao += 1
                x += 1
                em_validacao = False
            else:
                x = 0
                linhas_exp -= 1
                passo = 2
                em_validacao = True

        # direita
        if passo == 2:
            if  x < linhas_exp:
                posicao += colunas
                x += 1
                em_validacao = False
            else:
                x = 0
                colunas_exp -= 1
                passo = 3
                em_validacao = True

        # baixo
        if passo == 3:
            if x < colunas_exp:
                posicao -= 1
                x += 1
                em_validacao = False
            else:
                x = 0
                linhas_exp -= 1
                passo = 4
                em_validacao = True

        # esquerda
        if passo == 4:
            if x < linhas_exp:
                posicao -= colunas
                x += 1
                em_validacao = False
            else:
                x = 0
                passo = 1
                colunas_exp -= 1
                em_validacao = True

    posicoes[key] = posicao

# exibe expiral
ordem_expiral = dict(sorted(posicoes.items(), key=lambda item: item[1]))

pulo = 0
for i in ordem_expiral.keys():
    pulo += 1
    print(str(i).rjust(4),end='')

    if pulo == colunas:
        print('')
        pulo = 0

