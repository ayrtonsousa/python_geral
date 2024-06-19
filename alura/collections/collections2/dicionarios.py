from collections import defaultdict, Counter


aparicoes = dict(Ayrton = 1, cachorro = 2) #forma menos comum
print(aparicoes)

#forma mais comum
aparicoes = {
    "Ayrton": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

print(type(aparicoes))

print(aparicoes["cachorro"])
print(aparicoes.get('chave_que_nao_exite', 0))
print(aparicoes.get('Ayrton', 0))

aparicoes['alura'] = 'teste'
print(aparicoes)
del aparicoes['alura']
print(aparicoes)

print('cachorro' in aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

print(1 in aparicoes.values())

for chave, valor in aparicoes.items():
    print(chave, valor)

print(["palavra {}".format(elemento) for elemento in aparicoes])

meu_texto = 'Apenas um teste por que gosto de fazer testes no meu texto de bla bla bla'
meu_texto = meu_texto.lower()

#contando quantidade de aparicoes
aparicoes = {}
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)

#usando defaultdict
aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)

dicionario = defaultdict(int)
dicionario['teste']
print(dicionario) 

#usando o Counter para contar numero de aparicoes
print(Counter(meu_texto.split()))

#usando defaultdict em objetos
class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)

print(len(contas)) # nenhuma conta criada 
contas[15] 
print(len(contas)) # aparece uma nova conta
print(contas)


# Combinar dicionarios

from collections import ChainMap

# forma convencional
merged_dict = {}
dict1 = {"id": 1}
dict2 = {"name": 2}
dict3 = {"description": "teste teste"}

for d in (dict1, dict2, dict3):
    merged_dict.update(d)

print(merged_dict)

# usando ChainMap
merged_dict = dict(ChainMap(dict1, dict2, dict3))

print(merged_dict)