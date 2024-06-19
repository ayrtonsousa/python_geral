class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"Este é um carro da marca {self.marca}, modelo {self.modelo}."

    @classmethod
    def sedan(cls, marca_carro, modelo_carro):
        # o primerio parametro será o cls que é obrigatorio(como o self tambem é)
        # aqui passamos os parametros da classe, onde a func 'descricao' tera acesso
        # aqui tambem poderiamos acessar outras funcoes da classe
        return cls(marca_carro, f"{modelo_carro} Sedan")

    @staticmethod
    def hello_world():
        return 'hello world'
    
# Criando uma instância da classe Carro (onde precisa instanciar a classe antes)
carro1 = Carro("Toyota", "Corolla")
print(carro1.descricao())

# Chamando o método de classe (usamos a classe mas sem precisar instanciar diretamente)(comum usar em classes de model para chamar methodos crud)
carro2 = Carro.sedan("Honda", "Civic")
print(carro2.descricao())

# Chamando o método estatico (onde não precisa instanciar nada) 
msg = Carro.hello_world()
print(msg)


class Point:
    ...

class Point2:
    ...


p = Point()
p.z = 1995
p.y = 100

# tipo objeto
print(type(p))

# se e da instancia
print(isinstance(p, Point))
print(isinstance(p, Point2))

# se atributo existir
print(hasattr(p, 'z'))
print(hasattr(p, 'w'))

try:
    x = p.x
except AttributeError:
    print('Error attribute')



