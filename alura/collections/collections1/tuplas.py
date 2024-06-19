conta = (1, 750)

#forma funcional com tuplas
def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

conta = deposita(conta)
print(conta)