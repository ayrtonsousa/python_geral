import zipfile,os

#Extrai todos os arquivos do zip
os.chdir('C:\\Users\\ayrto\\Downloads')
exampleZip = zipfile.ZipFile('teste.zip')
exampleZip.extractall()

#Extraindo unico arquivo
exampleZip.extract('python-3.6.7-amd64.exe')

#Extraindo para pasta especifica
exampleZip.extract('python-3.6.7-amd64.exe','C:\\Users\\ayrto\\Downloads\\nova')


exampleZip.close()
