import re

#exemplo simples
numeroTelRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = numeroTelRegex.search('Meu número é 415-555-4242.')
print('Número de telefone '+mo.group())
print()

#exemplo por grupos ()
numeroTelRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = numeroTelRegex.search('Meu número é 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group())
print()


#caso tenha (), fazer o escape \
numeroTelRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = numeroTelRegex.search('Meu número é (415) 555-4242.')
print(mo.group(1))
print()
