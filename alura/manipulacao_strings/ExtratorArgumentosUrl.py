class ExtratorArgumentosUrl:

    def __init__(self,url):
        if self.url_valida(url):
            self.url = url.lower()
        else:
            raise ValueError("Url inválida!")

    #adicionando metodo especial(ou magico) __len__ da classe python para retorna valor ao chamar len() na classe
    def __len__(self):
        return len(self.url)

    def __str__(self):
        moeda_origem, moeda_destino = self.extrai_argumentos()
        #representacao_string = f"Valor: {self.extrai_valor()}\nMoeda Origem:{moeda_origem}\nMoeda destino: {moeda_destino}"
        representacao_string = "Valor: {}\nMoeda Origem:{}\nMoeda destino: {}".format(self.extrai_valor(),moeda_origem,moeda_destino)
        return representacao_string

    #altera funcao ao comparar a instancia, ao fazer instancia1 == instancia2 que por padrão faz id(instancia1) == id(instancia2) sendo que id de classes sempre serão diferentes
    def __eq__(self,outra_instancia):
        return self.url == outra_instancia.url

    #exemplo de metodo estatico, sem precisar ser instanciado e sem precisar do self pois e usado direto da classe
    @staticmethod
    def url_valida(url):
        if url and url.startswith('https://bytebank.com'):
            return True
        else:
            return False

    def extrai_argumentos(self):

        moeda_destino_buscada = 'moedadestino='
        moeda_origem_buscada = 'moedaorigem='

        indice_inicial_moeda_origem  = self.encontra_indice_inicial(moeda_origem_buscada)
        indice_final_moeda_origem    = self.url.find("&")
        
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            indice_inicial_moeda_origem  = self.encontra_indice_inicial(moeda_origem_buscada)
            indice_final_moeda_origem    = self.url.find("&")
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        
        indice_inicial_moeda_destino  = self.encontra_indice_inicial(moeda_destino_buscada)
        indice_final_moeda_destino    = self.url.find("&valor")
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]
        
        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda):
        return self.url.find(moeda) + len(moeda)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino","real",1)

    def extrai_valor(self):
        indice_inicial_valor = self.encontra_indice_inicial("valor=")
        return self.url[indice_inicial_valor:]