import re

#exemplo buscando telefone
email1 = "Meu numero cel 91234-1234 e meu telefone fixo 4566-2342"
email2 = "fale comigo em 1234-1234"
email3 = "1234-1234 meu numero"

#padrao = "[0123456789][0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]"
#padrao = "[0-9]{4,5}[-][0-9]{4}"
padrao = "[0-9]{4,5}[-]*[0-9]{4}" #busca tendo hifen ou nao
retorno = re.findall(padrao,email1) 
print(retorno)

#Encontrar conversar que estao no padrao abaixo
padrao2 = '[e][0-9]{1,2} [s,t][0-9]{1,2}'

conversa1 = "Estou no e 1 t 3 de Naruto"
conversa2 = "O e02 t2 é o melhor de Rick and Morty"
conversa3 = "Eu parei GOT no e2 s3"
conversa4 = "Não gostei do ep4 t5 de Vikings"
conversa5 = "O melhor episódio de Boku no Hero é o e011 s02"

retorno1 = re.search(padrao2,conversa2)
print(retorno1.group())
retorno2 = re.search(padrao2,conversa3)
print(retorno2.group())

#buscar dia da semana e data hora nas 3 frases
frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"

padrao3 =  "[a-z]{1,20}[ ][0-9]{1,2}[h]"

retorno4 = re.search(padrao3,frase1)
print(retorno4.group())

retorno5 = re.search(padrao3,frase2)
print(retorno5.group())

retorno6 = re.search(padrao3,frase3)
print(retorno6.group())
