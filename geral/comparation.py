if 0 == 0:
    print('igual')

if 1 == 1:
    print('igual')

if 1 != 2:
    print('diferente')

if 1 == 1 and 2 == 2:
    print('sao iguais')

if 1 == 2 or 2 == 2:
    print('condicao or')

if None is None:
    print('é none')

if not False:
    print('not negacao')

if 2 > 1:
    print('maior')

if 1 >= 1:
    print('maior ou igual')

if 1 < 2:
    print('menor')

if 1 <= 2:
    print('menor ou igual')

if any((False, True, False, False)):
    print('existe true')

if all((True, True, True, True)):
    print('todos sao true')

if '1'.isnumeric():
    print('e numerico')

if 'nome'.islower():
    print('minusculo')

if 'TESTE'.isupper():
    print('maisculo')

if '7'.isnumeric():
    print('e numerico')

if isinstance('texto', str) and isinstance(123, int):
    print('sao das instancias corretas')

if not 'a123'.isdecimal():
    print('nao é numerico')

if '10'.isdecimal():
    print('e decimal')

# ternario
print('é true') if True else print('nao e false')

