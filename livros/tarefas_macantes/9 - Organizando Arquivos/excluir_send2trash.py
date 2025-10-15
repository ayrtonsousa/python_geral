import send2trash

#Cria arquivo para o teste
baconFile = open('bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

#excluir arquivo utilizando send2trash, pois ele envia para lixiera onde é possível recuperar, no python padrão e excluído permanentemente
send2trash.send2trash('bacon.txt')