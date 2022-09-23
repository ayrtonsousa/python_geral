# 3.13 cria conjunto caracters latin-1 que tenham a palavra sign em seus nomes unicode

from unicodedata import name

print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})


# exemplos n mostrados que estao no livro sao exemplos mostrando questao de eficiencia gerando
# milhoes de dados e convertando para dict,set,list comparando o tempo de tabela hash deles
# mostrando que consomem muita memoria overhead mas sao muito rapidos
# 3.17 preenche 3 dicts com dados ordenados de maneira diferente, msm assim comparando da true

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

d1 = dict(DIAL_CODES)
print(d1.keys())
d2 = dict(sorted(DIAL_CODES))
print(d2)
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print(d3)
assert d1 == d2 and d2 == d3 #nao da erro pois sao iguais

# DICA: ao modificar dict em um iteravel modificar todos de uma vez com update, senao mudara a ordem e bagunçar tudo