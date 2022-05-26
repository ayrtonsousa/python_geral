import re

#Adicionar varias regras em multiplas linhas
phoneRegex = re.compile(r'''(

    (\d{3}|\(\d{3}\))?           #código da área
    (\s|-|\.)?                   #separador
    \d{3}                        #primeiros 3 digitos
    (\s|-|\.)                    #separador
    \d{4}                        #ultimos 4 digitos
    (\s*(ext|x|ext.)\s*\d{2,5})? #extensao
    )''', re.VERBOSE)

#Combinando ignorecase, dotall e verbose
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)