#Cria arquivo caso nao exista e sobrescreve se existir
baconFile = open('bacon.txt','w')
baconFile.write('Hello world!\n')
baconFile.close()

#Adiciona texto a arquivo aberto
baconFile = open('bacon.txt','a')
baconFile.write('Bacon não é vegetal!\n')
baconFile.close()

#Leitura do arquivo do exemplo
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)