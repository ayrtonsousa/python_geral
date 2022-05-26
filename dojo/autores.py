# Quando se lista o nome de autores de livros, artigos e outras publicações é comum que se apresente o nome do autor ou dos autores da seguinte forma:
# sobrenome do autor em letras maiúsculas, seguido de uma vírgula e da primeira parte do nome apenas com as iniciais maiúsculas.

# Por exemplo:

# SILVA, Joao
# COELHO, Paulo
# ARAUJO, Celso de
# Seu desafio é fazer um programa que leia um número inteiro correspondendo ao número de nomes que será fornecido, e, a seguir, 
# leia estes nomes (que podem estar em qualquer tipo de letra) e imprima a versão formatada no estilo exemplificado acima.

# As seguintes regras devem ser seguidas nesta formatação:
# o sobrenome será igual a última parte do nome e deve ser apresentado em letras maiúsculas;
# se houver apenas uma parte no nome, ela deve ser apresentada em letras maiúsculas (sem vírgula): se a entrada for “ Guimaraes” , 
# a saída deve ser “ GUIMARAES”;
# se a última parte do nome for igual a "FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA" ou "JUNIOR" e houver duas ou mais partes antes,
# a penúltima parte fará parte do sobrenome. Assim: se a entrada for "Joao Silva Neto", a saída deve ser "SILVA NETO, Joao" ;
# se a entrada for "Joao Neto" , a saída deve ser "NETO, Joao";
# as partes do nome que não fazem parte do sobrenome devem ser impressas com a inicial maiúscula e com as demais letras minúsculas;
# "da", "de", "do", "das", "dos" não fazem parte do sobrenome e não iniciam por letra maiúscula.

sobrenomes_ignorados = ["filho", "filha", "neto", "neta", "sobrinho", "sobrinha", "junior"]
nao_faz_parte = ["Da", "De", "Do", "Das", "Dos"]

nome = input('Entre com o nome:\n')

nome_tratado = nome.lower()
nome_list = nome.split(' ')


#ignorar os 'sobrenomes_ignorados'
if nome_list[-1] in sobrenomes_ignorados:
    del nome_list[-1]

# verifica tamanho do sobrenome e 
if len(nome_list) == 1:
    print(nome_list[0].upper())
else:
    # trata sobrenome
    sobrenome = nome_list[-1].upper()

    # capitula restante do nome
    nome_sem_sobrenome = ' '.join(nome_list[:-1]).title()

    # trata restante do nome para descapitular o que deve ignorar a capitulacao
    sem_sobrenome_list = nome_sem_sobrenome.split()
    sem_sobrenome_tratado = list(map(lambda x: x.lower() if x in nao_faz_parte else x, sem_sobrenome_list))
    nome_sem_sobrenome_tratado = ' '.join(sem_sobrenome_tratado)
    print(sobrenome, ', ', nome_sem_sobrenome_tratado, sep='')