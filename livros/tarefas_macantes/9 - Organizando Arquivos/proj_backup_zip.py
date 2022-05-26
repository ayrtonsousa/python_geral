#! python3
# backupToZip.py
# Copia uma pasta toda e seu conteudo para um arquivo zip cujo nome seja incrementado

import zipfile, os

def backupToZip(folder):
    # Faz backup do conteudo de folder em um arquivo zip

    folder = os.path.abspath(folder) # garante que folder e um path absoluto

    # Determina nome do arquivo que esse código deverá usar de acordo com os arquivos ja existentes
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Cria arquivo zip
    print('Criando %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Percorre toda arvore do diretorio e compacta arquivos de cada pasta
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adicionando arquivos em %s...' % (foldername))

        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Feito')


backupToZip('C:\\Users\\ayrto\\OneDrive\\Documentos\\tarefas_macantes\\5 - Dicionários')
