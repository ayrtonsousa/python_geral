from .personagem_base import PersonagemBase
from .decorators import checa_energia


class Cavaleiro(PersonagemBase):

    @checa_energia(custo_energia=30)
    def ataque_basico(self):        
        return 'Espadada normal'

    @checa_energia(custo_energia=50)
    def ataque_especial(self):
        return 'Espadada especial'

    def itens_iniciais(self):
        itens_cavaleiro = {
            'espada_afiada': 1
        }
        self.inventario.update(itens_cavaleiro)
        return super().itens_iniciais()