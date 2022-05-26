from classe_personagens.factory import get_classe_personagem
from classe_personagens.injection_dependency import ataque_fogo
from classe_personagens.observers import VidaStatusObserver, FimJogoObserver


classe_personagem = get_classe_personagem('mago')
personagem1 = classe_personagem('Ayrton', 26)
personagem1.attach(VidaStatusObserver())
personagem1.attach(FimJogoObserver())

print(personagem1)
print(personagem1.ataque_basico())
print(personagem1.ataque_especial_extra(ataque_fogo(personagem1)))
print(personagem1.ataque_especial())

personagem1.dano(10)
personagem1.dano(40)
personagem1.dano(45)
personagem1.dano(10)
