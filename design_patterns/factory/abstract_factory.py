from abc import ABCMeta, abstractmethod


# AbstractFactory
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        ...

    @abstractmethod
    def criar_pizza(self):
        ...


# ConcretFactoryA
class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaCamarao()


# ConcretFactoryB
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocolis()

    def criar_pizza(self):
        return PizzaBolonha()


# AbstractProdutoA
# Pizza vegana sera considera como base para as pizzas comuns mas sem a carne
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, PizzaVeg):
        ...


# AbstractProdutoB
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, PizzaVeg):
        ...

# ProdutoConcreto
class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')


# ProdutoConcreto
class PizzaCamarao(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com camarão na {type(PizzaVeg).__name__}')


# ProdutoConcreto
class PizzaBrocolis(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')


# ProdutoConcreto
class PizzaBolonha(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com bolonhesa na {type(PizzaVeg).__name__}')


# Cliente
class Pizzaria:

    def fazer_pizzas(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg()
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)

pizzaria = Pizzaria()
pizzaria.fazer_pizzas()