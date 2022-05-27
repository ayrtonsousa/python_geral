# EXPRESSOES CONDICIONAIS

def factorial(n):
    # forma extensa
    # if n == 0:
    #     return 1
    # else:
    #     return n * factorial(n-1)

    #forma mais concisa
    return 1 if n == 0 else n * factorial(n-1)


class Circle:
    def __init__(self, name, contents=None):
        self.name = name
        self.contents = [] if contents == None else contents


# ABRANGENCIA DE LISTAS
def capitalize_all(t):

    #res = []
    #for s in t:
    #    res.append(t.capitalize())
    #return res
    return [s.capitalize() for s in t]

def only_upper(t):
    # res = []
    # for s in t:
    #     if s.isupper():
    #         res.append(s)
    # return res
    return [s for s in t if s.isupper()]


# EXPRESSOES GERADORAS

g = (x**2 for x in range(5))

# depois da funcao next, for começara da posicao 3
print(next(g))
print(next(g))

print('Laço for:')
for val in g:
    print(val)

# ANY e ALL
print(any([False, True, False]))
print(any(letter == 'z' for letter in 'monty'))

def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

print(all([True, True, True]))

#CONJUNTOS

def subtract(d1, d2):
    # res = dict()
    # for key in d1:
    #     if key not in d2:
    #         res[key] = None
    # return res
    return set(d1) - set(d2)

def has_duplicates(t):
    # d = {}
    # for x in t:
    #     if x in d:
    #         return True
    #     d[x] = True
    # return False
    return len(set(t)) < len(t)

def uses_only(word, available):
    # for letter in word:
    #     if letter not in available:
    #         return False
    # return True
    return set(word) <= set(available)

# CONTADORES
from collections import Counter

count = Counter('parrot')
print(count)

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

# DEFAULTDICT
from collections import defaultdict
from inspect import signature

d = defaultdict(list)
t = d['new key']
print(t)
t.append('new value')
print(t)

def all_anagrams(filename):
    d = defaultdict(list)
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d[t].append(word)
    return d

# TUPLAS NOMEADAS

from collections import namedtuple

# Uma forma de criar classes 'simples'
Point = namedtuple('Point', ['x', 'y'])

p = Point(1,2)
print(p.x, p.y)

# ARGUMENTOS CHAVE (args e kwargs)
def printall(*args, **kwargs):
    print(args, kwargs)

printall(1, 2.0, third=3)

# usando classe
d = dict(x=1, y=2)
#point_classe = Point(d) #forma errada, onde ele passaria somente 1
point_classe = Point(**d)
print(point_classe)