from abc import ABC, abstractmethod
import json
import csv


class Exportacao(ABC):

    @abstractmethod
    def exportar(self, dados: str):
        ...


class CSVExportacao(Exportacao):

    def exportar(self, dados: str) -> None:
        """ Exporta resultados para CSV """
        with open('arquivos/resultado.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(dados)


class JSONExportacao(Exportacao):

    def exportar(self, dados: str) -> None:
        """ Exporta resultados para Json """
        dados_json = json.dumps({'resultados': dados})
        with open('arquivos/resultado.json', 'w') as f:
            f.write(dados_json)
