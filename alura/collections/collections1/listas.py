idades = [10, 27, 48, 60]

idades.append(26)

print('Idades adicionado 5 ao final', idades)

print('Pegando index[1]', idades[1])

idades.extend([12, 26])
print('Idades mais idades 26 e 12', idades)

idades.remove(26)
print('Removendo primeira ocorrencia de 26', idades)

idades.insert(0, 3)
print('Adiciona pelo index lista', idades)

idades_copy = idades.copy()
print('Copiando list', idades_copy)

idades_copy.clear()
print('Limpando list', idades_copy)

idades_mais_1 = [idade+1 for idade in idades]
print('Idades + 1', idades_mais_1)

idades_maior_27 = [idade for idade in idades if idade > 27]
print("Somente idades maiores que 27", idades_maior_27)

def diminui_1(idade):
    return idade - 1

idades_maior_27_menos_1 = [diminui_1(idade) for idade in idades if idade > 27]
print("Subtrai 1 de idades maiores que 27", idades_maior_27_menos_1)

#lista com problema, onde ira duplicar o valor devido a variavel lista estar em memoria
def teste_lista_problema(lista = []):
    lista.append(13)
    print(lista)

teste_lista_problema()
teste_lista_problema()
teste_lista_problema()

#solucao para funcao acima, criando none e verificando antes de adicionar
def teste_lista_solucao(lista = None):
    if lista is None:
        lista = []
    lista.append(13)
    print(lista)

teste_lista_solucao()
teste_lista_solucao()
teste_lista_solucao()