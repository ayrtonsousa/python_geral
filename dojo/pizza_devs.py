# Em algumas empresas de desenvolvimento de software é comum, quando o prazo de entrega de uma aplicação está próximo,
# a equipe passar algumas noites trabalhando. E como todo desenvolvedor também precisa se alimentar, eles sempre pedem pizza nessas ocasiões. Só que sempre é uma briga para conseguir escolher os sabores das pizza de sabores que todos gostam.

# Um dos membros da equipe, incomodado com as intermináveis discussões sobre o sabor a ser escolhido,
# resolveu desenvolver um programa para facilitar essa escolha.

# Para cada sabor de pizza disponível, cada um deve indicar uma nota para ele (nota 1, se a pessoa detesta o sabor e nota 5 se a pessoa adora o sabor).
# Depois de processar esses dados, cada pessoa vai saber quais as pessoas que tem o gosto mais parecido que o seu
# (e que provavelmente irá dividir uma pizza com você).

# Por exemplo, para os dados a seguir, o Luca gostaria de saber quem ele deve convidar para dividir uma pizza com ele:

# Renato = { Marguerita : 4, Quatro queijos : 5, Escarola : 4, Portuguesa : 5, Frango+Catupiry : 4, Napolitana : 3 }
# Marcelo = { Marguerita : 2, Quatro queijos : 2, Escarola : 1, Portuguesa : 3, Frango+Catupiry : 5, Napolitana : 2 }
# Lenon = { Marguerita : 4, Quatro queijos : 5, Escarola : 2, Portuguesa : 1, Frango+Catupiry : 1, Napolitana : 3 }
# Renata = { Marguerita : 4, Quatro queijos : 5, Escarola : 1, Portuguesa : 1, Frango+Catupiry : 3, Napolitana : 4 }
# Washington = { Marguerita : 1, Quatro queijos : 1, Escarola : 2, Portuguesa : 3, Frango+Catupiry : 4, Napolitana : 3 }
# Tino = { Marguerita : 1, Quatro queijos : 5, Escarola : 1, Portuguesa : 4, Frango+Catupiry : 3, Napolitana : 2 }
# Luca = { Marguerita : 5, Quatro queijos : 4, Escarola : 3, Portuguesa : 4, Frango+Catupiry : 3, Napolitana : 2 }

# Devs

dict_devs = {
    'marcelo': {
        'Marguerita': 2,
        'Quatro queijos': 2,
        'Escarola': 1,
        'Portuguesa': 3,
        'Frango+Catupiry': 5,
        'Napolitana': 2
    },
    'lenon': {
        'Marguerita': 4,
        'Quatro queijos': 5,
        'Escarola': 2,
        'Portuguesa': 1,
        'Frango+Catupiry': 1,
        'Napolitana': 3
    },
    'renata': {
        'Marguerita': 4,
        'Quatro queijos': 5,
        'Escarola': 1,
        'Portuguesa': 1,
        'Frango+Catupiry': 3,
        'Napolitana': 4
    },
    'renato': {
        'Marguerita': 4,
        'Quatro queijos': 5,
        'Escarola': 4,
        'Portuguesa': 5,
        'Frango+Catupiry': 4,
        'Napolitana': 3
    },
    'washington': {
        'Marguerita': 1,
        'Quatro queijos': 1,
        'Escarola': 2,
        'Portuguesa': 3,
        'Frango+Catupiry': 4,
        'Napolitana': 3
    },
    'tino': {
        'Marguerita': 5,
        'Quatro queijos': 5,
        'Escarola': 1,
        'Portuguesa': 4,
        'Frango+Catupiry': 3,
        'Napolitana': 2
    },
    'luca': {
        'Marguerita': 5,
        'Quatro queijos': 3,
        'Escarola': 3,
        'Portuguesa': 5,
        'Frango+Catupiry': 3,
        'Napolitana': 2
    }
}


#pega maior pizza
def maiores_notas(notas):
    pizzas = {}
    maior_nota = 0
    pizza_avaliada = ''
    notas_ordenadas = sorted(notas.items(), key=lambda x: x[1], reverse=True)

    for pizza, nota in notas_ordenadas:
        if nota >= maior_nota:
            maior_nota = nota
            pizza_avaliada = pizza
            pizzas[pizza_avaliada] = maior_nota
    
    return pizzas

# minhas maiores notas
minhas_notas = maiores_notas(dict_devs.pop('luca'))

# busca pizza com maiores notas dos devs
gosto_parecido = {}
for dev in dict_devs:
    maiores_notas_dev = maiores_notas(dict_devs[dev])
    gosto_parecido[dev] = {}

    # itera com notas com maior nota de cada dev
    for pizza, nota in maiores_notas_dev.items():
        # itera maiores notas de cada dev com as minhas maiores e adiciona ao dicionario
        for minha_pizza, minha_nota in minhas_notas.items():
            if nota >= minha_nota and pizza == minha_pizza:
                gosto_parecido[dev][pizza] = nota

    # caso vazio
    if gosto_parecido[dev] == {}:
        del gosto_parecido[dev]

# busca maior ocorrencia
maior_ocorrencia = 0
for dev in gosto_parecido:
    if len(gosto_parecido[dev]) > maior_ocorrencia:
        maior_ocorrencia = len(gosto_parecido[dev])


# remove os ocorrencia menor
resultado = {}
for dev in gosto_parecido:
    if len(gosto_parecido[dev]) >= maior_ocorrencia:
        resultado[dev] = gosto_parecido[dev]

# exibe dev com notas
print(resultado)