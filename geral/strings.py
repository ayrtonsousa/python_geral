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

my_str = "Teste meu Teste TESTANDO"

print('abc' * 3)

print('abc' + 'def')

print(my_str.replace('t','x'))

print(my_str.capitalize())
print(my_str.title())
print(my_str.upper())
print(my_str.lower())

print(len(my_str))


#buscando pelo inicio
print(my_str.startswith('Test'))
print(my_str.startswith('test'))
print(my_str.startswith('xyz'))

#buscando pelo fim
print(my_str.endswith('ANDO'))
print(my_str.endswith('ando'))
print(my_str.endswith('xyz'))

# retorna posicao da primeira ocorrencia
print(my_str.find('meu'))

# explode e o join de strings
print(my_str.split(' '))
print(';'.join(['boa','tarde']))

# conta ocorrencias
print(my_str.count('T'))

# retorna todas as letras
import string 
print(string.ascii_letters)

