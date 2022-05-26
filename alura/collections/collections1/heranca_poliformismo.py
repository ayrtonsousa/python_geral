from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>> Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass


conta_16 = ContaCorrente(16)
conta_16.deposita(1000)

conta_17 = ContaPoupanca(17)
conta_17.deposita(1000)

contas = [conta_16, conta_17]
for conta in contas:
    conta.passa_o_mes() #duck typing

for conta in contas:
    print(conta)

try:
    ContaInvestimento(123)
except Exception as e:
    print('Metodo nao foi implementado:', e)

