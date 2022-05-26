import re

#Identificar partes que tenham numeros com virgula a cada 3 numeros
#regra = re.compile(r'^\d{1,3}(,\d{3})*$')
#retorno = regra.findall('42 1,234 6,349,432 7,333,454')
#print(retorno)

#exe 22
regra = re.compile(r'(Ayrton|Cleiton|Reinaldo)\s(come|bebe|chuta)\s(maças|vinho|bola)\.',re.I)
retorno = regra.search('Ayrton bebe vinho.')
print(retorno.group())
