from .personagem_base import PersonagemBase
from .decorators import checa_energia


class Mago(PersonagemBase):

    @checa_energia(custo_energia=30)
    def ataque_basico(self):        
        print('Cajadada')

    @checa_energia(custo_energia=50)
    def ataque_especial(self):
        print('Cajadada Especial')

    def itens_iniciais(self):
        super().itens_iniciais()
        itens_mago = {
            'pocao_magia': 1
        }
        self.inventario.update(itens_mago)
        return self.inventario
    