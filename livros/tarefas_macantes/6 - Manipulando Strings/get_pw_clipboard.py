#! python3
#pw.py um programa de senhas que nao e seguro

PASSWORDS = {'email':'123mudar','blog':'***ayrton***','facebook':'123Mudar!'}

import sys,pyperclip

if len(sys.argv) < 2:
    print('Uso: python pw.py [conta] -copia senha da conta no dicionar')
    sys.exit()

conta = sys.argv[1] #o primeiro argumento da linha de comando e nome da conta

if conta in PASSWORDS:
    pyperclip.copy(PASSWORDS[conta])
    print('Senha da '+ conta + ' copiado para a área de transferência.')
else:
    print('Isso não é o nome de uma das contas')