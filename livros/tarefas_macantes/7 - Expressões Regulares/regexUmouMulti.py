import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
print()

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
print()

mo3 = batRegex.search('The Adventures of Batman')
print(None if mo3 == None else True)
print()