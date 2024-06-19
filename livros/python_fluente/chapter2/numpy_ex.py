import numpy

a = numpy.arange(12)
print(a)
print(type(a))

a.shape = 3, 4
print(a)

print(a[2])
print(a[2, 1])
print(a[:, 1])
print(a.transpose()) # troca linha pelas colunas

# exemplo tratando operacoes alto nivel carregar, salvar e realizar operacoes em todos os elementos de um numpy.ndarray

floats = numpy.loadtxt('floats-10M-lines.txt') # exemplo de um arquivo a ser importado, somente de exemplo
print(floats[-3:])
floats *= .5
print(floats[-3:])

from time import perf_counter as pc

t0 = pc(); floats /= 3; pc() - t0
print(t0)

numpy.save('floats-10M', floats)

floats2 = numpy.load('floats-10M.npy', 'r+')
floats2 *= 6
print(floats2[-3:])
