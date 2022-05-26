from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, personagem):
        """ Recebe atualizacao do personagem"""
        ...


class VidaStatusObserver(Observer):
    def update(self, personagem):
        mensagem = ''
        if personagem.vida >= 50:
            mensagem = "Vida normal"
        elif personagem.vida > 25:
            mensagem = "Vida baixa"
        elif personagem.vida > 10:
            mensagem = "Vida muito baixa"
        elif personagem.vida >= 1:
            mensagem = "Você está morrendo, tome uma poção!"
        print(mensagem)

            
class FimJogoObserver(Observer):
    def update(self, personagem):
        if personagem.vida == 0:
            print("Você morreu, fim de jogo")        