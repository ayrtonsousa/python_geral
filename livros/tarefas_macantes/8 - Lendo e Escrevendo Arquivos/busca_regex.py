import os, re

#Valor ser buscado
print('Indique a palavra a ser buscada:')
valor = str(input())

#Lista arquivos de texto
os.chdir('.\\arquivos')           # Entra na pasta dos arquivos
diretorio = os.getcwd()           # Caminho dos arquivos 
lista_arq = os.listdir(diretorio) # Cria Lista com arquivos

#Cria list com cada arquivo
for arquivo in lista_arq:
    dados = open(arquivo)
    linha_lista = dados.readlines()

    #Passa por cada linha
    for linha in linha_lista:
        linha = linha.replace('\n','')
        regexBusca = re.compile(valor)
        resul = regexBusca.search(linha)
        if resul != None:
            print(linha)



    