import re
from abc import ABC, abstractmethod


class RegexInterface(ABC):

    @abstractmethod
    def aplica_regex(self, dados: str) -> str:
        ...


class RegexTelefone(RegexInterface):

    def aplica_regex(self, dados: str) -> str:
        """ Busca padrão de telefone """
        padrao = "[(]*[0-9]{2}[)]*[ ]*[0-9]{4,5}[-]*[0-9]{4}"
        resposta = re.findall(padrao, dados)
        return resposta
