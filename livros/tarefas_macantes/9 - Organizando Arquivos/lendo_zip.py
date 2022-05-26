import zipfile, os

os.chdir('C:\\Users\\ayrto\\Downloads')

#Le arquivos dentro do zip
exampleZip = zipfile.ZipFile('teste.zip')
print(exampleZip.namelist())

#tamanho de arquivo dentro do zip
spamInfo = exampleZip.getinfo('python-3.6.7-amd64.exe')
print(spamInfo.file_size)
print(spamInfo.compress_size)

print('Compressed file is %sx smaller'  % (round(spamInfo.file_size/spamInfo.compress_size, 2)))


exampleZip.close()