from .decorators import checa_energia


@checa_energia(custo_energia=40)
def ataque_fogo(self):
    return 'Ataque de fogo'

@checa_energia(custo_energia=40)
def ataque_gelo(self):
    return 'Ataque de gelo'