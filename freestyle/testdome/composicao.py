# Uma TrainComposition é construída acoplando e desprendendo vagões dos lados esquerdo e direito,  de forma eficiente  em relação ao tempo utilizado.

# Por exemplo, se começarmos ligando o vagão 7 pela esquerda e depois prendendo o vagão 13, novamente pela esquerda, 
# obtemos uma composição de dois vagões (13 e 7 da esquerda para a direita). 
# Agora o primeiro vagão que pode ser destacado pela direita é o 7 e o primeiro que pode ser destacado pela esquerda é o 13.

# Implemente um TrainComposition que modele esse problema.

class TrainComposition:
    
    def __init__(self):
        self.lista = []
    
    def attach_wagon_from_left(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the left
        """
        self.lista.insert(0, wagonId)

    
    def attach_wagon_from_right(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the right
        """
        self.lista.append(wagonId)

    def detach_wagon_from_left(self):
        """
        :returns: (int) The number of the wagon detached from left
        """
        if self.lista:
            return self.lista.pop(0)
    
    def detach_wagon_from_right(self):
        """
        :returns: (int) The number of the wagon detached from right
        """
        if self.lista:
            return self.lista.pop(-1)

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13