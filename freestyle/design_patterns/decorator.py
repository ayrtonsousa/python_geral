from abc import ABC, abstractmethod


class Pao(ABC):

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @abstractmethod
    def valor(self):
        ...


class Frances(Pao):

    def __init__(self):
        self._nome = 'Francês'

    def valor(self):
        return 2

class Baguete(Pao):

    def __init__(self):
        self._nome = 'Baguete'

    def valor(self):
        return 3


class RecheioDecorator(Pao):
    def valor(self):
        ...


class Salame(RecheioDecorator):

    def __init__(self, pao: Pao):
        self._pao = pao

    @property
    def nome(self):
        return self._pao.nome + ", salame"

    def valor(self):
        return 1 + self._pao.valor()
    

class Calabresa(RecheioDecorator):

    def __init__(self, pao: Pao):
        self._pao = pao

    @property
    def nome(self):
        return self._pao.nome + ", calabresa"

    def valor(self):
        return 2 + self._pao.valor()
    
if __name__ == '__main__':
    frances = Frances()
    frances = Salame(frances)
    print(frances.nome, frances.valor())

    baguete = Baguete()
    baguete = Salame(baguete)
    baguete = Calabresa(baguete)
    """abaixo ao chamar a property, ele roda cada instancia decorada"""
    print(frances.nome, frances.valor())
    print(baguete.nome, baguete.valor())