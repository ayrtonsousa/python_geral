# Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.

# O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

# As regras são as seguintes:

# Pedra empata com Pedra e ganha de Tesoura
# Tesoura empata com Tesoura e ganha de Papel
# Papel empata com Papel e ganha de Pedra


from random import randint


print('ESCOLHA UMA DAS OPÇÕES ABAIXO:')
print('''
    (1) - PAPEL
    (2) - TESOURA
    (3) - PEDRA
''')

opcoes = {
    1: 'PAPEL',
    2: 'TESOURA',
    3: 'PEDRA'
}


print('Jogador 1:')
while True:
    try:
        escolha_jogador1 = int(input('Escolha uma opção acima:\n'))
        break
    except:
        print('Opção não disponível escolha outra !')


print('Computador:')
escolha_jogador2 = randint(1,3)

# 0 empate, 1 jogador, computador
print(f'{opcoes[escolha_jogador1]} X {opcoes[escolha_jogador2]}')
if escolha_jogador1 == escolha_jogador2:
    vencedor_partida = 0
elif (escolha_jogador1 - escolha_jogador2) in [-2,1]:
    vencedor_partida = 1
else:
    vencedor_partida = 2

print('Fim de jogo !')

if vencedor_partida == 1:
    print('Jogador 1 venceu !')
elif vencedor_partida == 2:
    print('Computador venceu !')
else:
    print('Empate')