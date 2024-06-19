import re

#ocorrencia opcional wo ou man
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
print()


mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())