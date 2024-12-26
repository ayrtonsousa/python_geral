from abc import ABCMeta, abstractmethod


class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar_fonte(self):
        ...
    
    @abstractmethod
    def compilar_objeto(self):
        ...
    
    @abstractmethod
    def executar(self):
        ...

    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.executar()


class CompiladorIOS(Compilador):

    def coletar_fonte(self):
        print('Coletando codigo fonte Swift')
    
    def compilar_objeto(self):
        print('Compilado codigo swift para bytecode LLVM')
    
    def executar(self):
        print('Programa executando no ambiente de execucao')


class CompiladorAndroid(Compilador):

    def coletar_fonte(self):
        print('Coletando codigo fonte Kotlin')
    
    def compilar_objeto(self):
        print('Compilado codigo Kotlin para bytecode JVM')
    
    def executar(self):
        print('Programa executando no ambiente de execucao')


ios = CompiladorIOS()
ios.compilar_e_executar()

android = CompiladorAndroid()
android.compilar_e_executar()
    
    
