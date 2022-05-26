import re

#Guarda dados do arquivo
vfile = open('C:\\Users\\ayrto\\OneDrive\\Documentos\\tarefas_macantes\\8 - Lendo e Escrevendo Arquivos\\madexample.txt')
vContent = vfile.read()

#Substitui valores na primeira ocorrencia
print('Substitua adjective por:')
nova = str(input())
vContent = vContent.replace('ADJECTIVE',nova,1)

print('Substitua noun por:')
nova = str(input())
vContent = vContent.replace('NOUN',nova,1)

print('Substitua verb por:')
nova = str(input())
vContent = vContent.replace('VERB',nova,1)

print('Substitua noun por:')
nova = str(input())
vContent = vContent.replace('NOUN',nova,1)

print(vContent)

#Salva novo arquivo
baconFile = open('madexampleedit.txt','w')
baconFile.write(vContent)
baconFile.close()

