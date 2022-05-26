import os

#percorre estrutura de pasta
for folderName, subFolders, fileNames in os.walk('C:\\Users\\ayrto\\OneDrive\\Imagens'):
    print('The current folder is ' + folderName)

    for subfolder in subFolders:
        print('Subfolder of '+folderName+': '+subfolder)

    for filename in fileNames:
        print('File Inside'+folderName+': '+filename)

    print()
