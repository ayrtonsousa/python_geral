import shutil, os

#exclui permanentemente os arquivos
for filename in os.listdir():
    if filename.endswith('.rtx'):
        #os.unlink(filename)
        print(filename)    

