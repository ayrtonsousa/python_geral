a = (1,2,3)

# nao altera dados na tupla
#a[0] = 4

# mas atributos de objetos, dict, etc sim !
a = (1,2,3,{'chave':'valor'},3,3,3)
a[3]['chave'] = 'novo valor'
print(a)

# mostra valor pela posicao
print(a.index(2))

# ocorrencias do numero 3
print(a.count(3))