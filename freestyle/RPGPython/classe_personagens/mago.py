from .personagem_base import PersonagemBase
from .decorators import checa_energia


class Mago(PersonagemBase):

    @checa_energia(custo_energia=30)
    def ataque_basico(self):        
        return 'Cajadada'

    @checa_energia(custo_energia=50)
    def ataque_especial(self):
        return 'Cajadada Especial'

    def itens_iniciais(self):
        itens_mago = {
            'pocao_magia': 1
        }
        self.inventario.update(itens_mago)
        return super().itens_iniciais()
    