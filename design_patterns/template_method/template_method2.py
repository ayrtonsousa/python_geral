from abc import ABCMeta, abstractmethod


class ClasseAbstrata(metaclass=ABCMeta):

    def __init__(self):
        ...

    @abstractmethod
    def operacao1(self):
        pass

    @abstractmethod
    def operacao1(self):
        pass

    def template_method(self):
        print('Definindo o algoritmo: operacao 2 e depois a 1')
        self.operacao2()
        self.operacao1()


class ClasseConcreta(ClasseAbstrata):

    def operacao1(self):
        print('operacao 1')

    def operacao2(self):
        print('operacao 2')


class Cliente:

    def main(self):
        self.concreta = ClasseConcreta()
        self.concreta.template_method()


cliente = Cliente()
cliente.main()