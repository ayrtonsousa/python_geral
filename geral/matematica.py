import math

a = 5
b = 2

# soma
print(a + b)
print(a.__add__(b))

print(sum([1,2,3]))

# subtrair
print(a - b)
print(a.__sub__(b))

# multiplicar
print(a * b)
print(a.__mul__(b))

# dividir
print(a/b)
print(a.__truediv__(b))

numero = 1
numero += 1
print('somar variavel', numero)
numero -= 5
print('subtrair variavel', numero)

# pegar inteiro do valor da divisao
print('pega inteiro do resultado da divisao', 100 // 3)
# pegar o resto do valor divisao
print('pega o resto da divisao', 100 % 3)
# pegar inteiro do valor diretamente
print('pega inteiro do valor', 7.50 // 1)
# pegar o resto do valor diretamente
print('pega o resto', 7.50 % 1)

# potenciação 3 * 3 * 3
print(3**3)

# arredonda 2 casas decimais acima do 0.49
print(round(9.5049, 2))
print(round(9.5050, 2))
print(round(9.5060, 2))
print(round(9.10))
print(round(9.49))
print(round(9.51))

# arredondar sempre pra cima
print(math.ceil(10.49))
print(math.ceil(10.50))
print(math.ceil(10.55))

# para sempre pra baixo
print(math.floor(10.49))
print(math.floor(10.50))
print(math.floor(10.55))

print(max((33,1,10,99,80)))

print(min((31,2,13,96,70)))


# nao colocar zero a esquerda (problema provavelmente por numero  binario, hex ou octa)
#exemplo = 0304
