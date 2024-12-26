usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

#criando um conjunto (set), nao exibindo os elementos repetidos
print(set(assistiram))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_machine_learning)
print(type(usuarios_machine_learning))

#usuarios_machine_learning_set[3] dará erro pois nao existe ordem em conjuntos, a ordem pode variar
for usuario in usuarios_data_science:
    print(usuario)

#exibindo somente os elementos que existem nos 2, sem duplicadas
print(usuarios_data_science | usuarios_machine_learning)

#exibindo somente elementos que existem entre si
print(usuarios_data_science & usuarios_machine_learning)

#removendo elementos que existam nas duas listas
print(usuarios_data_science - usuarios_machine_learning)

#exibindo somente elementos exclusivos que nao existem nos outros conjuntos
print(usuarios_data_science ^ usuarios_machine_learning)


#adicionando elementos no conjunto
usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))

#que ja existe
usuarios.add(13)
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))

#congelando valores de conjuntos para ficarem imutaveis
usuarios = frozenset(usuarios)
print(type(usuarios))

#usuarios.add(15) irá dar erro pois o frozenset e imutavel

meu_texto = 'Apenas um teste por que gosto de fazer testes no meu texto de bla bla bla'

meu_texto_set = set(meu_texto.split())
print(meu_texto_set)