import re

#Busca se no inicio do texto existe a palavra
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello World!'))
print(beginsWithHello.search('He said hello.'))
print()

#Busca regra no final do texto
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Meu numero e 11991077149'))
print()

#Busca que tenha regra no inicio e final
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12   34567890') == None)

#Caracter Coringa busca qualquer palavra (exceto quebra de linha)
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)
print()

#Caracter Coringa com asterisco busca tudo exceto broken line
atRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = atRegex.search('First Name: Ayrton Moises Last Name: Sousa')
print(mo.group(1))
print(mo.group(2))
print()

#Diferenca greedy e nongreedy
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
print()

#Passando parametro de quebra de linha

#Exemplo sem
regexLinha = re.compile('.*')
mo = regexLinha.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)

#Exemplo com
regexLinha = re.compile('.*', re.DOTALL)
mo = regexLinha.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)