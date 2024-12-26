# se contem

s1 = 'abcd'
s2 = 'cd'

print(s1.__contains__(s2))

# formatar
fruta_a = 'maça'
fruta_b = 'banana'
print(f'uma {fruta_a} e um {fruta_b}')
print('uma {} e um {}'.format(fruta_a, fruta_b))

# centralizar
print('vou centralizar'.center(150))

print('abc' * 3)

print('abc' + 'def')

my_str = "Teste meu Teste TESTANDO"

print(my_str.replace('t','x'))

print(my_str.capitalize())
print(my_str.title())
print(my_str.upper())
print(my_str.lower())

# tamanho de caracteres
print(len(my_str))

# conta somente ocorrencias de caracteres
print(my_str.count('T'))

# retorna posicao da primeira ocorrencia
print(my_str.find('meu'))

#buscando pelo inicio
print(my_str.startswith('Test'))
print(my_str.startswith('test'))
print(my_str.startswith('xyz'))

#buscando pelo fim
print(my_str.endswith('ANDO'))
print(my_str.endswith('ando'))
print(my_str.endswith('xyz'))

# explode e o join de strings
print(my_str.split(' '))
print(';'.join(['boa','tarde']))

# retorna todas as letras do alfabeto
import string 
print(string.ascii_letters)

