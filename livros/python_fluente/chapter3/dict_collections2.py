dicionario = {'a': 1, 'b': 2, 'c': 3}

# mostra ultimo item
print(dicionario.popitem())

# remove ultimo item (NAO FUNCIONA NAS VERSOES MAIS RECENTES)
#dicionario.popitem(last=True)


import builtins
from collections import ChainMap, Counter, UserDict

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

# exemplo nao e do livro mas para melhor entendimento, onde se faz a busca de n dicts de 1 vez
# se key duplicada mostra o 1

alpha_num = ChainMap(numbers, letters)
print(alpha_num["two"])


print(alpha_num.get("a"))

# counter para dicionarios
ct = Counter('abracadabra')
print(ct)

ct.update('aaaaazzz')
print(ct)
print(ct.most_common(2)) # 2 mais comuns

# 3.8 converte chaves nao str para str na insercao, consulta e atualizacao

class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

dict_str = StrKeyDict([('1', 'one'), ('2', 'two')])
print(dict_str)
print(dict_str[1])
dict_str[1] = 'um'
print(dict_str[1])
dict_str[3] = 'three'
print(dict_str)

# 3.9 (n adicionei por acha especifico) classe MutableMapping para deixar imutavel o mapeamento(bom para hardware fisico n ser modificado por ex.)