from validate_docbr import CPF, CNPJ


class DocumentoFactory:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return CPFDocumento(documento)
        elif len(documento) == 14:
            return CNPJDocumento(documento)
        else:
            raise ValueError("Documento inválido!")


class CPFDocumento:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formata()

    def valida(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos errada")

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
  

class CNPJDocumento:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.formata()

    def valida(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos errada")

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
