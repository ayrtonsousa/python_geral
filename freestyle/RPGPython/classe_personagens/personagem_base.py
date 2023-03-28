from abc import ABCMeta, abstractmethod


class PersonagemBase(metaclass=ABCMeta):

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = self._checa_idade(idade)
        self._vida = 100
        self._energia = 100
        self._forca = 0
        self._magia = 0
        self._inventario = {}
        self._observadores = []

        self.itens_iniciais()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        self._checa_idade(value)
        self._idade = value

    def _checa_idade(self, value):
        """ Verifica idade mínima e máxima """
        if value < 10:
            raise ValueError('Idade deve ser maior que 10')
        elif value > 60:
            raise ValueError('Idade deve ser menor que 60')

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        self._vida = value

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, value):
        self._energia = value

    @property
    def forca(self):
        return self._forca

    @forca.setter
    def forca(self, value):
        self._forca = value

    @property
    def magia(self):
        return self._magia

    @magia.setter
    def magia(self, value):
        self._magia = value

    @property
    def inventario(self):
        return self._inventario

    @inventario.setter
    def inventario(self, dict_itens):
        self._inventario.update(dict_itens)

    @abstractmethod
    def ataque_basico(self):
        "Ataque básico do personagem"
        ...

    @abstractmethod
    def ataque_especial(self):
        "Ataque especial do personagem"
        ...

    def ataque_especial_extra(self, funcao=None):
        "Ataque especial extra do personagem"
        if funcao:
            return funcao
        return 'Sem ataque especial extra!'

    def itens_iniciais(self):
        """ Itens iniciais do personagem """
        itens = {
            'pocao_vida': 1,
            'pocao_cura_veneno': 1
        }
        self.inventario.update(itens)
        return self.inventario

    def attach(self, observer):
        """ Vincular a um observer """
        print(
            f"Personagem vinculado a observer: {observer.__class__.__name__}"
        )
        self._observadores.append(observer)

    def detach(self, observer):
        """ Desvincular a um observer """
        self._observadores.remove(observer)

    def _notifica(self):
        """ Atualiza cada observador """
        for observer in self._observadores:
            observer.update(self)

    def dano(self, value):
        """ Reduz vida com base no dano recebido """
        print("Personagem sofreu dano !")
        if  value <= self.vida:
            self.vida -= value
            print(f"Sua vida mudou para: {self.vida}")
        else:
            self.vida = 0
        self._notifica()

    def __str__(self):
        return self.nome