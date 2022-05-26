dadosTabela = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def exibeTabela(dados):
    larguraCol = []
    celulaCol = 4

    #define largura coluna
    for linha in range(len(dados)):
        larguraColIni = 0
        for item in dados[linha]:
            if len(item) > larguraColIni:
                larguraColIni = len(item)
        larguraCol.append(larguraColIni)

    #monta linhas
    for linha in range(celulaCol):#loop por linha
        for item in range(len(dados)):
            print(dados[item][linha].rjust(larguraCol[item]+2),end='')
        print()

exibeTabela(dadosTabela)


"""
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    colWidth = 0
    for l in range(len(list)):
        for s in range(len(list[l])):
            if len(list[l][s]) > colWidth:
                colWidth = len(list[l][s])
    for l in range(len(list)):
        for s in range(len(list[l])):
            print(list[l][s].rjust(colWidth + 2), end = '')
        print()
    
printTable(tableData)
"""