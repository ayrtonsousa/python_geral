

class Instalador:

    def __init__(self, fonte, destino):
        self.opcoes = []
        self.destino = destino
        self.fonte = fonte

    def preferencias(self, escolha):
        self.opcoes.append(escolha)

    def executar(self):
        for opcao in self.opcoes:
            if list(opcao.values())[0]:
                print(f'Copiando os binarios de {self.fonte} para {self.destino}')
            else:
                print('Operacao finalizada')


if __name__ == '__main__':
    # inicia instalador
    instalador = Instalador('python3.9.1.gzip', '/usr/bin/') # dados ficticios

    # O usuario escolhe instalar apenas o Python
    instalador.preferencias({'python': True})
    instalador.preferencias({'java': False})

    # Execute
    instalador.executar()
