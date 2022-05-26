import shutil, os

os.chdir('C:\\Users\\ayrto\\OneDrive\\Documentos\\tarefas_macantes\\9 - Organizando Arquivos')

shutil.copy('testecopia.txt','.\\novapasta')               #copia para nova pasta
shutil.copy('testecopia.txt','.\\novapasta\\novonome.txt') #copia passando novo nome

#copia pasta completa
shutil.copytree('C:\\Users\\ayrto\\OneDrive\\Documentos\\tarefas_macantes\\9 - Organizando Arquivos\\novapasta','C:\\Users\\ayrto\\OneDrive\\Documentos\\tarefas_macantes\\9 - Organizando Arquivos\\novapastabackup') 
