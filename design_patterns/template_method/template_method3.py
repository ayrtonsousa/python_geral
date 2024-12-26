from abc import ABCMeta, abstractmethod


class Viagem(metaclass=ABCMeta):

    @abstractmethod
    def ida(self):
        pass
    
    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass 

    @abstractmethod
    def retorno(self):
        pass

    def itinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()


class ViagemVeneza(Viagem):

    def ida(self):
        print('Viagem de aviao...')
    
    def dia1(self):
        print('Visita a basilica de sao marcos na praça sao marcos')

    def dia2(self):
        print('Visita ao palacio Doge')

    def dia3(self):
        print('Aproveitar a comida proximo a ponte Rialto')

    def retorno(self):
        print('Viagem de avião...')


class ViagemMalvinas(Viagem):

    def ida(self):
        print('Viagem onibus...')
    
    def dia1(self):
        print('Apreciar vida marinha de Banana Reef')

    def dia2(self):
        print('Praticar esportes aquaticos')

    def dia3(self):
        print('Relaxar na praia')

    def retorno(self):
        print('Viagem de aviao...')


class GeekTravel:

    def preparar_viagem(self):
        opcao = input("Qual viagem ? [veneza, malvinas]:\n")
        
        if opcao == 'veneza':
            self.viagem = ViagemVeneza()
            self.viagem.itinerario()
        elif opcao == 'malvinas':
            self.viagem = ViagemMalvinas()
            self.viagem.itinerario()
        else:
            print('opcao invalida')


agencia = GeekTravel()
agencia.preparar_viagem()