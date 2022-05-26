import array as arr
import numpy as np

#criando array tipo d(float)
arr_float = arr.array('d', [1, 3.5])
print(arr_float)

try:
    arr.array('d', [1, 3.5, 'Texto'])
except Exception as e:
    print('Erro por possuir tipo diferente:',e)

#usando numpy, e comum evitar array do python e utilizar p numpy para arrays
numeros = np.array([1, 3.5])
print(numeros)

print(numeros + 3)
