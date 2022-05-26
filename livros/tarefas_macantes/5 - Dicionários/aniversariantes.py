aniversariantes = {'Kirito':'12/12/1990','Asuna':'08/07/1988','Sinon':'02/03/1992'}


while True:
    print("Informe o nome do aniversariante")
    nome = input()

    if nome == '':
        break
    else:
        if nome not in aniversariantes:
            print(f"Aniversariante {nome} não existe no dicionário, gostaria de adicioná-lo?")
            print("Digite 'S' para adicionar e 'N' para cancelar")
            resposta = input()

            if resposta == 'S':
                print("Informe a data de aniversário dd/mm/YYYY")
                dataaniv = input()
                aniversariantes.setdefault(nome,dataaniv)
                print('Aniversariante incluído com sucesso!')
                continue

        else:
            print('Aniversário do',nome,'é em',aniversariantes[nome])
            continue




