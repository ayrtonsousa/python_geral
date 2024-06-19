import forca
import adivinhacao

def escolha():
    print("*********************************")
    print("*******Escolha seu jogo!*********")
    print("*********************************")

    print("Adivinhação(1), Forca(2)")

    jogo = int(input("Qual o jogo?"))

    if jogo == 1:
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif jogo == 2:
        print("Jogando Forca")
        forca.jogar()

if __name__ == '__main__':
    escolha()