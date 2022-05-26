import re

#busca maior string possivel de acordo com regra
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
print()

#busca menor string possivel de acordo com regra
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
print()