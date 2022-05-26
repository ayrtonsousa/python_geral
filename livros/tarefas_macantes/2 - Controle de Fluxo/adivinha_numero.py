import random

numero_secreto = random.randint(1,10)

print("Informe um número entre 1 e 10")
print("Você tera 5 tentativas")
print("Boa Sorte")


for i in range(5,-1,-1):
    numero = input("Informe um número:")

    try:
        numero = int(numero)
        if numero_secreto == numero:
            print(f"Parabéns você acertou o número é: {numero_secreto}")
            print("Fim de Jogo")
            break
        else:
            if numero_secreto < numero:
                print("Número secreto é menor")
            else:
                print("Número secreto é maior")

        if i < 1:
            print("O número era",numero_secreto)
            print("Fim de Jogo")
        else:
            print(f"Você tem mais {i} tentativa(s)")        

    except:
        print("Digite somente números!")
        if i < 1:
            print("O número era",numero_secreto)
            print("Fim de Jogo")
        else:
            print(f"Você tem mais {i} tentativa(s)")  





