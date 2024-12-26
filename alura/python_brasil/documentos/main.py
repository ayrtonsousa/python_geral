from documentos.cpf import DocumentoFactory


cpf = DocumentoFactory.cria_documento('03082840035')
cnpj = DocumentoFactory.cria_documento('36660837000104')

print(cpf)
print(cnpj)