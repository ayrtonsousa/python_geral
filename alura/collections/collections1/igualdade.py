class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Codigo {} Saldo {}".format(self._codigo, self._saldo)

class ContaSalario2:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Codigo {} Saldo {}".format(self._codigo, self._saldo)

class ContaHeranca(ContaSalario):
    ...

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1 == conta2)
print(conta1 in [conta2])
print(conta2 in [conta1])

conta1.deposita(1)

print(conta1 == conta2)

conta1 = ContaSalario(37)
conta2 = ContaSalario2(37)

print(conta1 == conta2)

#checa se instancia e da classe especifica
print(isinstance(conta1, ContaSalario))

#checa se instancia de classe filha e igual classe mae
conta3 = ContaHeranca(13)
print(isinstance(conta3, ContaSalario))