# Funcionários de empresas comerciais que trabalham como caixa tem uma grande responsabilidade em suas mãos.
# A maior parte do tempo de seu expediente de trabalho é gasto recebendo valores de clientes e, em alguns casos, fornecendo troco.

# Seu desafio é fazer um programa que leia o valor total a ser pago e o valor efetivamente pago,
# informando o menor número de cédulas e moedas que devem ser fornecidas como troco.

# Deve-se considerar que há:

# cédulas de R$100,00, R$50,00, R$20,00, R$10,00, R$5,00 e R$2,00;
# moedas de R$1.00, R$0,50,  R$0,25, R$0,10, R$0,05.

cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05]
troco_moedas = []
troco_cedulas = []


valor_compra = 153.36
valor_pago = 160

# valor_compra = 100.56
# valor_pago = 1000

if valor_pago < valor_compra:
    print("Valor pago menor que compra")
elif valor_pago == valor_compra:
    print("Valor igual, sem troco")
else:
    troco = round(valor_pago - valor_compra,2)
    resto_cedulas = troco // 1
    resto_moedas = round(troco % 1, 2)
    #6,64

    # troco moedas, se for abaixo de 0.05 NÃO da troco de 0.01 centavos
    while resto_moedas >= 0.05:
        for moeda in moedas:
            if moeda <= resto_moedas:
                troco_moedas.append(moeda)
                resto_moedas -= moeda
                break

    # troco cedulas
    while resto_cedulas > 1:
        for cedula in cedulas:
            if cedula <= resto_cedulas:
                troco_cedulas.append(cedula)
                resto_cedulas -= cedula
                break

    # se sobrar 1 real, joga como troco moeda
    if resto_cedulas == 1:
        troco_moedas.append(1)

    print('Cédulas:', troco_cedulas)
    print('Moedas:', troco_moedas)
    print('Resto pra bala?:', round(resto_moedas,2))

    print('Total-Pago:', troco)
    print('Igual a Total-Pago?', round(sum(troco_cedulas) + sum(troco_moedas) + round(resto_moedas,2),2))
