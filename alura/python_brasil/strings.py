from collections import defaultdict
import random

#nome invertido e em letras maisculas
def nome_invertido_upper():
    nome = input("Entre com seu nome \n")
    nome = nome.lower().upper()
    print('Invertido',nome[::-1])

#imprimir nome na vertical e em escada
def nome_vertical_escada(inverso=False):
    nome = input("Informe seu nome \n")
    posicao = 0
    for letra in nome:
        posicao = posicao - 1 if inverso else posicao + 1
        print(nome[:posicao])


#formata data por extenso
def data_extenso():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
            'Agosto', 'Setembro', 'Novembro', 'Dezembro']
    data = input("Informe sua data de nascimento em dd/mm/yyyy\n")
    data_list = data.split('/')
    print("Você nasceu em {} de {} de {}".format(data_list[0],meses[int(data_list[1]) - 1],data_list[2]))

#conta vogais e espacos em branco
def conta_vogais_espacos_branco():
    frase = input("Entre com uma frase: ")
    frase_list = list(frase.lower())
    letras = defaultdict(int)
    for letra in frase_list:
        if letra in 'aeiou' or letra == ' ':
            letras[letra] += 1
    print(letras)

def checa_palindromo():
    frase = input("Digite frase palindromo: ")
    frase_sem_espacos = ''.join(frase.lower().split(' '))
    frase_invertida = ''.join(reversed(frase_sem_espacos))
    if frase_sem_espacos == frase_invertida:
        print('Palindromo')
    else:
        print("não e palindromo")

def jogo_da_forca():
    palavras = ['maça', 'laranja', 'uva']
    letras_digitadas = []

    palavra_secreta = random.choice(palavras)
    tentativas = 0
    limite_tentativas = 3
    print("Jogo da forca")
    texto = '_' * len(palavra_secreta)

    while True:
        print("Palavra: ", texto)
        letra_digitada = input("Digite uma letra: ")
        letras_digitadas.append(letra_digitada)
        
        if letra_digitada in palavra_secreta:
            print("Acertou!")
            texto_lista = list(texto)
            index = 0
            for letra in palavra_secreta:
                if letra_digitada == letra:
                    texto_lista[index] = letra_digitada
                index += 1
            texto = ''.join(texto_lista)
            if texto == palavra_secreta:
                print("Parabéns, você acertou a palavra secreta !")
                break
        else:
            print("Errou, tente novamente")
            tentativas += 1

        if tentativas > 3:
            print("Fim de jogo")
            print(f"palavra secreta era: {palavra_secreta}")
            break
        else:
            print(f"Você ainda tem {limite_tentativas-tentativas }")
            

def valida_cpf():
    cpf = input("Informe seu cpf em formato xxx.xxx.xxx-xx: ")
    cpf = cpf.strip().replace('.', '').replace('-', '')
    if len(cpf) < 11:
        print("CPF incompleto")
        return False
    cpf = [int(numero) for numero in cpf]
    primeiro_digito_verificador = cpf[-2]
    segundo_digito_verificador = cpf[-1]

    calculo_primeiro_digito = (cpf[0] * 10 + cpf[1] * 9 + cpf[2] * 8 + cpf[3] * 7 + cpf[4] * 6 + cpf[5] * 5 
                    + cpf[6] * 4 + cpf[7] * 3 + cpf[8] * 2)
    resto_calculo_primeiro_digito =  (calculo_primeiro_digito * 10) % 11

    calculo_segundo_digito = (cpf[0] * 11 + cpf[1] * 10 + cpf[2] * 9 + cpf[3] * 8 + cpf[4] * 7 + cpf[5] * 6 
                    + cpf[6] * 5 + cpf[7] * 4 + cpf[8] * 3 + cpf[9] * 2)
    resto_calculo_segundo_digito = (calculo_segundo_digito * 10) % 11

    if resto_calculo_primeiro_digito != primeiro_digito_verificador or resto_calculo_segundo_digito != segundo_digito_verificador:
        print('CPF inválido!')
    else:
        print('CPF válido')

    
def corrige_formato_telefone():
    telefone = input("Informe seu telefone fixo: ")
    telefone = telefone.replace('-', '')
    qtd_caracteres = len(telefone)

    if qtd_caracteres < 8:
        print(f"Telefone possui {qtd_caracteres} dígitos. Vou acrescentar o digito três na frente")
        diferenca = 8 - qtd_caracteres
        telefone = '3' * diferenca + telefone

    print(f"Telefone corrigido sem formatação: {telefone}")
    telefone = telefone[:4] + '-' + telefone[4:]
    print(f"Telefone corrigido com formatação: {telefone}")
     
    
#repeticao
#listas
#funcoes
#classes