dados = {
    'escola': {
        'nome': 'Escola São Paulo'
    },
    'alunos': [
        {'nome': 'Pablo', 'idade': 12},
        {'nome': 'Vitor Bueno', 'idade': 11},
        {'nome': 'Volpi', 'idade': 13},
    ]
}

# print(dados['escola'])
# print(dados['alunos'][1]['nome'])


# for item in dados.keys():
#     print(item)

# for item in dados.values():
#     print(item)

# for key,value in dados.items():
#     print(key,value)

# for aluno in dados['alunos']:
#     print(aluno['nome'])

# def by_value(item):
#     return item['idade']

# for aluno in sorted(dados['alunos'], key=by_value, reverse=True):
#     print(aluno['nome'], aluno['idade'])

print(list(filter(lambda item: 'V' in item['nome'], dados['alunos'])))

help(print)