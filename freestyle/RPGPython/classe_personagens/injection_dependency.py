from .decorators import checa_energia


@checa_energia(custo_energia=40)
def ataque_fogo(self):
    print('Ataque de fogo')

@checa_energia(custo_energia=40)
def ataque_gelo(self):
    print('Ataque de gelo')