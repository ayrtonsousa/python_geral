import re

#exemplo usando outras classes de caracters
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 loards, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rigs, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

#passando caracters especificos
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo2 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)

#passando caracters para negação
vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo2 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)