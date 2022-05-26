pessoas = {'Ayrton':{'bolacha':2,'bebida':1,'paes':1},'Cleiton':{'bebida':3},'Regina':{'frios':2,'paes':1},'Reinaldo':{'frutas':1}}

def conta_itens(dicionario):
    itens = {}
    for pessoa,coisas in dicionario.items():
        for desc,qtd in coisas.items():
            itens.setdefault(desc,0)
            itens[desc] = itens[desc] + qtd

    print('Itens quantidade de itens trazidos por cada pessoa:')
    for descricao,valor in itens.items():
        print(descricao,':',valor)
    print('Total de itens :'+str(sum(itens.values()))) 

conta_itens(pessoas)

