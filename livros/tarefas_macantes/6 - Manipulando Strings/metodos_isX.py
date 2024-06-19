while True:
    print('Digite sua Idade')
    idade = input()
    if idade.isdecimal():
        break
    print('Por favor digite sua idade com números')

while True:
    print('Selecione uma senha (Somente Letras e Números)')
    password = input()
    if password.isalnum():
        break
    print('Senha pode conter letras e números')