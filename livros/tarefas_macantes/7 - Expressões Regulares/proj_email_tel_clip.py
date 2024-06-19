#! python
#Encontra telefones e email no clipboard

import pyperclip, re

#regex telefone
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?             #código da área
    (\s|-|\.)?                     #separador
    (\d{3})                        #primeiros 3 digitos
    (\s|-|\.)                      #separador
    (\d{4})                        #ultimos 4 digitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extensao
    )''', re.VERBOSE)

#regex email
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)

#texto do clipboard (area de transferencia)
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
    
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copiado para área de transferência')
    print('\n'.join(matches))
else:
    print('Não há números de telefone ou emails encontrados')