from .cavaleiro import Cavaleiro
from .mago import Mago

from .constantes import CLASSE_PERSONAGEM_CAVALEIRO, CLASSE_PERSONAGEM_MAGO



def get_classe_personagem(classe_personagem):
    """ Busca classe do personagem """
    if classe_personagem == CLASSE_PERSONAGEM_CAVALEIRO:
        return Cavaleiro
    elif classe_personagem == CLASSE_PERSONAGEM_MAGO:
        return Mago
    else:
        raise NotImplementedError('Classe de personagem não existe')