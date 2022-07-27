from factory import factory_method_exportacao, factory_method_regex


class LerRegexEmArquivo:
    def __init__(self, arquivo: str, regex: str) -> None:
        self.arquivo = arquivo
        self.regex = regex
        self.dados_original = self.__le_arquivo()
        self.dados_regex = self.__aplica_regex()

    def __le_arquivo(self) -> str:
        """ Lê arquivo """
        with open(self.arquivo, 'r') as arquivo:
            return arquivo.read()

    def __aplica_regex(self) -> None:
        """ Aplica regex a dados do arquivo """
        classe = factory_method_regex(self.regex)
        return classe.aplica_regex(self.dados_original)

    def exportacao(self, tipo: str) -> None:
        """ Exporta resultados """
        classe = factory_method_exportacao(tipo)
        classe.exportar(self.dados_regex)
