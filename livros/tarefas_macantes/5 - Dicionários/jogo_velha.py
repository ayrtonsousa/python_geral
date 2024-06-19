tabuleiro_base = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}

def exibeTabuleiro(tabua):
    print(tabua['top-L'] + '|' + tabua['top-M'] + '|' + tabua['top-R'])
    print(tabua['mid-L'] + '|' + tabua['mid-M'] + '|' + tabua['mid-R'])
    print(tabua['low-L'] + '|' + tabua['low-M'] + '|' + tabua['low-R'])

turn = 'X'

#roda para cadaposicao
for i in range(9):
    exibeTabuleiro(tabuleiro_base)#exibe tabuleiro

    #pede proxima posicao
    print('Marcar', turn ,'em qual espaço?')   
    posicao = input()
    tabuleiro_base[posicao] = turn

    #troca sinal para proximo jogador
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'


exibeTabuleiro(tabuleiro_base)