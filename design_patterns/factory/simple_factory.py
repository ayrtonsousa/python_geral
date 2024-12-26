from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):

    def falar(self):
        print('au au!')


class Gato(Animal):

    def falar(self):
        print('miau!')


# Fabrica
class Fabrica:

    def criar_animal_falante(self, tipo):
        # eval para transformar string recebida como se fosse a instancia
        return eval(tipo)().falar()

# Cliente
if __name__ == '__main__':
    fabrica = Fabrica()
    animal = input("Qual animal vc quer que fale? [Cachorro,Gato]\n")
    fabrica.criar_animal_falante(animal)



