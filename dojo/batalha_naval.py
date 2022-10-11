# Cada jogador deve dispor de uma área de 10x10 onde ele vai posicionar 5 navios de tamanhos diferentes: um porta-aviões (comprimento 5), 
# um encouraçado (comprimento 4), 
# um submarino e um destroyer (ambom de comprimento 3),
# e barco de patrulha (comprimento 2).
# Um jogador nunca deve saber a posição dos navios do oponente.
# Os navios de um mesmo jogador não podem se cruzar e devem estar dentro das fronteiras da sua área disponível.

# Depois que todas as peças estão posicionadas, os jogadores se alternam em turnos para lançar bombas sobre o outro oponente especificando
# qual posição ele deseja atacar. Se algum dos navios do jogador que está sendo atacado estiver na posição atacada,
# considera-se que o navio foi atingido. O ataque falha se o atacante lançar uma bomba em um local onde não existe nenhum navio do oponente.

# Caso todos as posições de um navio for atingida, o jogador atacado deve informar o oponente qual dos seus navios afundou. 
# O jogo continua até que um jogador afunde todos os navios de seu oponente; este jogador é então considerado vencedor.

# Você deve desenvolver um programa que jogue uma partida de batalha naval entre dois oponentes. Você precisa:

# Definir uma maneira de indicar o estado inicial dos navios dos jogadores;
# Exibir todos os movimentos dos jogadores, informando se os ataques foram bem sucedidos ou não;
# Informar quando um navio é atingido e quando ele é afundado;
# Exibir ao final do jogo um mapa final do posicionamento final dos navios dos jogadores.



import random
import copy

""" Cria colunas e linhas """
linhas = {str(l):'-' for l in range(10)}
area = {str(c):linhas.copy() for c in 'ABCDEFGHIJ'}


def exibe_area(area_jogador):
    """ Exibe area jogador """
    for coluna in area_jogador.keys():
        print(coluna.rjust(4),end='')
    print('')
    print('-'*45)

    for linha in linhas.keys():
        print(linha, end='')

        for coluna in area_jogador.keys():
            print(str(area_jogador[coluna][linha]).rjust(4),end='')
            if coluna == 'J':
                print('')


def cria_navios_area():
    """ Adiciona navios na area """

    navios = {
        'porta_avioes': 5,
        'encouracado': 4,
        'submarino': 3,
        'destroyer': 3,
        'barco_patrulha': 2,
    }

    posicoes = {}

    # cria area
    linhas = {str(l):False for l in range(10)}
    area_navios = {str(c):linhas.copy() for c in 'ABCDEFGHIJ'}
    
    colunas = ['A','B','C','D','E','F','G','H','I','J']

    for navio, tamanho in navios.items():
        # distribui navios entre as colunas randomicamente
        coluna_aleatoria = random.choices(colunas)[0]
        colunas.remove(coluna_aleatoria)
        while True:
            # busca linha inicial para navio
            linha_aleatoria = random.randrange(0,10)

            # checa se navio cabe na coluna senao procura nova linha
            if linha_aleatoria > tamanho:
                continue
    
            for linha in area_navios[coluna_aleatoria].keys():
                if int(linha) >= linha_aleatoria and tamanho > 0:
                    area_navios[coluna_aleatoria][linha] = True
                    tamanho -= 1
            posicoes[navio] = {'coluna': coluna_aleatoria, 'tamanho': navios[navio]}
            break

    return area_navios, posicoes


def marca_ponto(area_adversario, area_navios_adversario, coluna, linha):
    """ Marca ponto na area """
    try:
        coordenada = area_adversario[coluna][linha]
    except:
        print('Coordenada inexistente')
        return

    if coordenada != '-':
        print('Local já marcado!')
    else:
        if area_navios_adversario[coluna][linha]:
            area_adversario[coluna][linha] = 'O'
            print('Acertou!')
        else:
            area_adversario[coluna][linha] = 'X'
            print('Tiro na água!')

def checa_navio(area, posicoes, ultima_coluna_jogada):
    """ Checa posicoes do adversario e se coluna jogada foi a ultima """
    for key, values in posicoes.items():
        if values['coluna'] == ultima_coluna_jogada:
            #checa se tamanho da area pontuada na coluna e do navio
            pontos = 0
            for i in area[ultima_coluna_jogada]:
                if area[ultima_coluna_jogada][i] == 'O':
                    pontos += 1
            if values['tamanho'] == pontos:
                print(f'{key} afundou!')
                posicoes.pop(key)
                # checa se posicoes foram todas descobertas
                if posicoes == {}:
                    return True
            break
    return False
    
# deepcopy sendo usando somente para fins didaticos, pois copy normal com itens mutaveis ele muda na copia e original!

jogador1 = copy.deepcopy(area)
navios_jogador1, posicoes_jogador1 = cria_navios_area()

jogador2 = copy.deepcopy(area)
navios_jogador2, posicoes_jogador2 = cria_navios_area()


while True:
    print('\nVez do jogador 1')
    coluna_input = str(input('Informe a coluna:\n')).upper()
    linha_input = input('Informe a linha:\n')
    marca_ponto(jogador2, navios_jogador2, coluna_input, linha_input)
    status_jogador_1 = checa_navio(jogador2, posicoes_jogador2, coluna_input)
    exibe_area(jogador2)

    print('\nVez do jogador 2')
    coluna_input2 = str(random.choices(['A','B','C','D','E','F','G','H','I','J'])[0])
    linha_input2 = str(random.randrange(0,10))
    print(f'informe a coluna:{coluna_input2}')
    print(f'informe a linha:{linha_input2}')

    marca_ponto(jogador1, navios_jogador1, coluna_input2, linha_input2)
    status_jogador_2 = checa_navio(jogador1, posicoes_jogador1, coluna_input2)

    if status_jogador_1:
        print('Fim de jogo! Jogador 1 venceu!')
        exibe_area(jogador2)
        break
    if status_jogador_2:
        print('Fim de jogo! Jogador 2 venceu!')
        exibe_area(jogador1)
        break