

class University(type):

    def __call__(cls, *args, **kwargs):
        """
        Quando objeto precisa ser criado para uma
        classe ja existente, onde a metaclasse
        agora controla a criacao do objeto
        """
        print(f'=== Estes sao argumentos: {args}')
        return type.__call__(cls, *args, **kwargs)

    
class Geek(metaclass=University):

    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2


obj = Geek(42,23)

print(obj)