# 2.21 alterando valor de um item do array ao mudar um de seus bytes

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)

print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers)