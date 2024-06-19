#ler arquivo
hellofile = open('C:\\Users\\ayrto\\OneDrive\\Documentos\\tarefas_macantes\\8 - Lendo e Escrevendo Arquivos\\hello.txt')
helloContent = hellofile.read()
print(helloContent)

#ler multiplas linhas
cancaofile = open('C:\\Users\\ayrto\\OneDrive\\Documentos\\tarefas_macantes\\8 - Lendo e Escrevendo Arquivos\\cancao.txt')
cancaoContent = cancaofile.readlines()
print(cancaoContent)