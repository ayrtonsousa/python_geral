from abc import ABCMeta, abstractclassmethod


class Pedido:
    
    def __init__(self, total) -> None:
        self.__total = total

    @property
    def total(self) -> int:
        return self.__total

    @total.setter
    def total(self, value) -> None:
        self.__total = value


# interface
class CalculaJurosStrategyInterface(metaclass=ABCMeta):
    
    @abstractclassmethod
    def taxa_de_juros(pedido: Pedido) -> int:
        ...

# strategy concret
class Santander(CalculaJurosStrategyInterface):
    def taxa_de_juros(self, pedido: Pedido) -> int:
        return 10

class Bradesco(CalculaJurosStrategyInterface):
    def taxa_de_juros(self, pedido: Pedido) -> int:
        return 20


# context
class CalculadoraDeJuros:

    def __init__(self, calculador_de_juros: CalculaJurosStrategyInterface):
        self.__calculador_de_juros = calculador_de_juros

    @property
    def calculador_de_juros(self) -> CalculaJurosStrategyInterface:
        return self.__calculador_de_juros

    @calculador_de_juros.setter
    def calculador_de_juros(self, value) -> None:
        self.__calculador_de_juros = value

    def calcula_juros(self, pedido: Pedido) -> int:
        return self.__calculador_de_juros.taxa_de_juros(pedido)


if __name__ == '__main__':
    pedido = Pedido(100)
    banco = Santander()
    calculadora = CalculadoraDeJuros(banco)
    print(calculadora.calcula_juros(pedido))

    pedido2 = Pedido(150)
    banco2 = Bradesco()
    calculadora2 = CalculadoraDeJuros(banco2)
    print(calculadora2.calcula_juros(pedido2))
