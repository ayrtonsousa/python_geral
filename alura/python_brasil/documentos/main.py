from documentos.cpf import DocumentoFactory



cpf = DocumentoFactory.cria_documento('43135397866')
cnpj = DocumentoFactory.cria_documento('36660837000104')

print(cpf)
print(cnpj)