while True:

    usuario = input("Digite seu usuário:")

    if usuario != 'ayrton':
        continue

    senha = input("Digite sua senha:")

    if senha == '123mudar':
        break


print('Bem vindo',usuario)