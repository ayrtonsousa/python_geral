from operator import attrgetter
from functools import total_ordering


@total_ordering
class ContaSalario():
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
        return "[>> Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo


conta1 = ContaSalario(34)
conta2 = ContaSalario(454)
conta3 = ContaSalario(12)

conta1.deposita(120)
conta2.deposita(300)
conta3.deposita(50)

contas = [conta1, conta2, conta3]

#ordenando usando funcao que pega saldo
def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    print(conta)

#forma sem funcao e evitando expor variavel privada pelo encapsulamento
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

#verificando se saldo e menor entre contas
print(conta1 < conta2)

"""verificando se saldo e maior entre contas, ao implementar o primeiro metodo de menor __lt__, ele faz 
o inverso, nao precisando criar o metodo de maior na classe"""
print(conta2 > conta3)

#agora ele faz a ordenacao natural depois de implementado o metodo __lt__
for conta in sorted(contas):
    print(conta)

for conta in sorted(contas, reverse=True):
    print(conta)


#ordenando, primeiro por saldo e depois por codigo
conta1 = ContaSalario(1700)
conta2 = ContaSalario(3)
conta3 = ContaSalario(133)

conta1.deposita(500)
conta2.deposita(500)
conta3.deposita(1000)

contas = [conta1, conta2, conta3]


for conta in sorted(contas, key=attrgetter("_saldo","_codigo")):
    print(conta)

conta1 = ContaSalario(1700)
conta2 = ContaSalario(3)
conta3 = ContaSalario(133)

#ordenando, primeiro por saldo e depois por codigo
conta1.deposita(500)
conta2.deposita(500)
conta3.deposita(500)

contas = [conta1, conta2, conta3]

#ordenando, primeiro por saldo e depois por codigo
for conta in sorted(contas):
    print(conta)


"""fazendo menor igual utilizando decorator total_ordering para não precisar criar outras funcoes de comparacao maior igual 
e aproveitar o __lt__ e __eq__ que estao implementadas
lembrando que ele compara o codigo tbm, entao mesmo saldo sendo igual ele pode dar False"""
print(conta1 >= conta2)
print(conta1 <= conta2)
print(conta1 == conta1)