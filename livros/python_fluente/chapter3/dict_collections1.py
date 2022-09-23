# 3.2 forma nao eficiente de buscar e atualizar valores com get 

""" Cria um indice que mapeia a palavra -> lista de ocorrencias no arquivo zen_python.txt """
import sys
import re

WORD_RE = re.compile('\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # isso n e elegante foi apenas para ilustrar a questao
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper):
    print(word, index[word])

# 3.3 use python dicts.py zen_python.txt para rodar o script

# 3.4 usando setdefault para buscar e atualizar ocorrencias do indice em uma unica linha
WORD_RE = re.compile('\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # usando setdefault
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

# 3.5 usando defaultdict ao inves de setdefault
import collections

WORD_RE = re.compile('\w+')

index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

# exibe em ordem alfabetica
for word in sorted(index, key=str.upper):
    print(word, index[word])

# 3.7 classe converte chaves que n sejam strings para str na consulta
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

# 3.6 buscar chave q nao seja string StrKeyDict0 a convertera para str se nao for encontrada(esta depois da 3.7 pra mostrar apos class ser criada)
d = StrKeyDict0([('2', 'two'), ('4', 'four')])

# usando d[key]
print(d['2'])
print(d[4])
#print(d[1]) # ira dar erro pois mesmo convertendo pra str ela n existira

# usando d.get(key) onde get da classe resolve o erro caso key n seja str
print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N/A'))

# usando in 
print(2 in d) # onde __contains__ da classe resolve o erro onde tando faz ser int ou str
print(1 in d) # n existe mesmo convertendo deve dar False
