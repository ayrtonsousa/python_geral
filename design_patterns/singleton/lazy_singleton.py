# singleton lazy faz que o objeto seja criado somente quando utilizado

class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('O metodo __init__ foi chamado...')
        else:
            print(f'A instancia ja foi criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton() # classe e iniciada, mas obj nao e criado

print(f'Objeto criado agora: {Singleton.get_instance()}')

s2 = Singleton() # instancia ja criada
