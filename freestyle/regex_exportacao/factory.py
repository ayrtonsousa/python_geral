from typing import Type

from exportacao import Exportacao, CSVExportacao, JSONExportacao
from regex import RegexInterface, RegexTelefone


def factory_method_regex(tipo: str) -> Type[RegexInterface]:
    """
    Retorna tipos de regex:
    tel: Telefone
    """

    tipos = {
        "tel": RegexTelefone,
    }

    return tipos[tipo]()


def factory_method_exportacao(tipo: str) -> Type[Exportacao]:
    """
    Retorna tipos de exportação:
    json: Exportação JSON
    csv: Exportação de CSV
    """
    tipos = {
        "csv": CSVExportacao,
        "json": JSONExportacao,
    }

    return tipos[tipo]()
