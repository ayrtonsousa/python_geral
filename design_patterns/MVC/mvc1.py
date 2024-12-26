

class Modelo:

    def __init__(self):
        self.produtos = {
            'xboxsx': {'id': 1, 'nome': 'Xbox Series X', 'preco': 3700},
            'ps5': {'id': 2, 'nome': 'Playstation 5', 'preco': 3000},
            'nswitch': {'id': 3, 'nome': 'Nintendo Switch', 'preco': 2300},
        }


class Controlador:

    def __init__(self):
        self.modelo = Modelo()
    
    def listar_produtos(self):
        produtos = self.modelo.produtos.keys()

        print('--------Produtos--------')
        for chave in produtos:
            print(f"ID:{self.modelo.produtos[chave]['id']}")
            print(f"ID:{self.modelo.produtos[chave]['nome']}")
            print(f"ID:{self.modelo.produtos[chave]['preco']}")
            print('')


class Visao:

    def __init__(self):
        self.controlador = Controlador()
    
    def produtos(self):
        self.controlador.listar_produtos()


if __name__ == '__main__':
    visao = Visao()
    visao.produtos()
    