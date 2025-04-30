import re

#Busca zero instancia de (wo)*
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
print()

#Busca em unica instancia
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print()

#Busca varias instancias
mo3 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo3.group())
print()