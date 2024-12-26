from classe_personagens.factory import get_classe_personagem
from classe_personagens.injection_dependency import ataque_fogo
from classe_personagens.observers import VidaStatusObserver, FimJogoObserver


if __name__ == '__main__':
    # Criação personagem
    classe_personagem = get_classe_personagem('mago')
    personagem1 = classe_personagem('Ayrton', 27)
    personagem1.attach(VidaStatusObserver())
    personagem1.attach(FimJogoObserver())

    # Dados básicos
    print(personagem1)
    print(f'Inventário: {personagem1.inventario}')

    # Gasta energia do personagem
    personagem1.ataque_basico()
    personagem1.ataque_especial_extra(ataque_fogo(personagem1))
    personagem1.ataque_especial()

    # Faz personagem receber danos até esgotar sua vida
    personagem1.dano(10)
    personagem1.dano(40)
    personagem1.dano(45)
    personagem1.dano(10)
