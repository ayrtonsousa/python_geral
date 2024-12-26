import meu_modulo

print(f'o nome e {meu_modulo.NOME}')

meu_modulo.funcao1()




import meu_modulo as mm 

mm.funcao2()


""" um modulo em Python faz o singleton 
onde mesmo reimportando e dando apelido
ao executar sera mostrado somente um print

"""