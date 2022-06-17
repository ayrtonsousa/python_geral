# atribuindo valores a fatias

l = list(range(10))
l[2:5] = [20, 30]
#print(l)
del l[5:7]
#print(l)
l[3::2] = [11, 22]
#print(l)

#l[2:5] = 100 # ira dar erro pois precisa ser iteravel

# usando + e *, sempre criam novo objeto, jamais modificam o mesmo

l = [1, 2, 3]
#print(l * 3)
#print(5 * 'abcdef')

"""
2.12 uma listcomps com tres listas de tamanho 3 representando jogo da velha

internamente ele ta fazendo isso:
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
"""
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

"""
2.13 um exemplo errado onde a lista referencia a mesma lista!

internamente ele ta fazendo isso:
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
"""
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

# nao muda endereco somente conteudo
l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l))

# muda endereco e conteudo menos eficiente pois precisa recriar e concatenar
l = (1, 2, 3)
print(id(l))
l *= 2
print(id(l))

# 2.14 dará erro mais ira concatenar
t = (1, 2, [30, 40])

try:
    t[2] += [50, 60]
except:
    print(t)