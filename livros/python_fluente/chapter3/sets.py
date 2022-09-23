# 3.10 conta ocorrencias entre needles e haystack ambos do tipo set
needles = set(['email1@gmail.com', 'email2@gmail.com', 'email3@gmail.com'])
haystack = set(['email1@gmail.com', 'email2@gmail.com'])

found = len(needles & haystack)

print(found)

# 3.11 conta ocorrencia sem usar &
found = 0

for n in needles:
    if n in haystack:
        found += 1
print(found)


# 3.12 conta ocorrencias de needles em haystack estas linhas funcionam para qualquer tipo iteravel
found = len(set(needles) & set(haystack))
print(found)

found = len(set(needles).intersection(haystack))
print(found)

# {} sera um dict use set() para definir um set VAZIO
print(type({}))
print(type(set()))

# bytecode das duas operacoes onde mostra que usando {1} ao inves de set([1]) e mais rapido
from dis import dis

dis('{1}')
dis('set([1])')

# frontset
print(frozenset(range(10)))