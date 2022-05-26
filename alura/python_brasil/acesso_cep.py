import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.formata()
    
    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_api(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf'],
        )

cep = '06852200'

objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
bairro, cidade, uf = objeto_cep.acessa_api()

print(bairro, cidade, uf)