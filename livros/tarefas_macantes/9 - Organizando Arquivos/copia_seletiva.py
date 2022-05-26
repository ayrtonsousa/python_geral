#Identifica extensao especifica dentro de diretorios e copia

import os,shutil

def copia_seletiva(extensao):
    
    #percorre estrutura de pasta identifica
    for folderName, subFolders, fileNames in os.walk('C:\\Users\\ayrto\\OneDrive\\Imagens'):
        #percorre cada arquivo
        for filename in fileNames:
            #identifica extensao desejada
            if filename.endswith(extensao):
                print('Caminho do arquivo: '+folderName+': '+filename)
                shutil.copy(os.path.join(folderName, filename),'C:\\Users\\ayrto\\Downloads\\novapasta')   #copia para nova pasta


copia_seletiva('.png')