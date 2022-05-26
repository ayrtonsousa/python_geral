class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {} <<]".format(self.codigo, self.saldo)


conta_1 = ContaCorrente(1)
conta_1.deposita(500)

conta_2 = ContaCorrente(2)
conta_2.deposita(1000)
contas = [conta_1, conta_2]

for conta in contas:
    print(conta)

#Exemplo de referencias, onde e referencia ao mesmo objeto, não criando um novo, por isso tomar cuidado ao modificar
contas = [conta_1, conta_2, conta_1]

contas[0].deposita(100)
print(contas[0])
contas[2].deposita(100)
print(contas[2])

def deposita_todas_as_contas(contas):
    for conta in contas:
        print(conta)
        conta.deposita(100)

deposita_todas_as_contas(contas)

print(contas[0],contas[1], contas[2])