# 2.20 criando e salvando e carregando array grande de numeros ponto flutuante(10 milhoes)
# outra forma de salvar numeros, tipo complex e ate instancia seria usar pacote pickle

from array import array
from random import random


floats = array('d', (random() for i in range(10**7)))

print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp) # 7x mais rapido pra criar comparado a arquivo de texto
fp.close()

floats2 = array('d') # cria um array vazio de doubles
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7) # le 10 milhoes de numeros do arquivo binario criado, quase 60x mais rapido que em arquivos de texto
fp.close()

print(floats2[-1])

print(floats == floats2)