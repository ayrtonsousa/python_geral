def chama_numeros():
    while True:
        try:
            x = int(input("Informe o primeiro número: "))
            break
        except ValueError:
            print("Informe somente números!")
    while True:
        try:
            y = int(input("Informe o segundo número: "))
            break
        except ValueError:
            print("Informe somente números!")
    return x, y

def soma():
    print("SOMA")
    x,y = chama_numeros()
    return x + y

def subtracao():
    print("SUBTRAÇÃO")
    x,y = chama_numeros()
    return x - y

def multiplicacao():
    print("MULTIPLICAÇÃO")
    x,y = chama_numeros()
    return x * y

def divisao():
    print("DIVISÃO")
    while True:
        try:
            x,y = chama_numeros()
            return  x / y
        except ZeroDivisionError:
            print("Não se pode dividor por zero!")
    
operacoes = {
    1 : soma,
    2 : subtracao,
    3 : multiplicacao,
    4 : divisao,
}


def get_operacao():
    print(
        """
        Selecione uma operação matemática
        (1) Soma
        (2) Subtração
        (3) Multiplicação
        (4) Divisão
        """
    )
    operacao_escolhida = int(input("Informe a operação: "))

    operacao = operacoes.get(operacao_escolhida, None)
    return operacao


while True:
    operacao = get_operacao()
    if operacao:
        resultado = operacao()
        print('Resultado da operação foi: {}'.format(resultado))
        print('Operação realizada')
        break
    else:
        print('Escolha uma operação existente!')
