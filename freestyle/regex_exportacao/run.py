from ler_arquivo import LerRegexEmArquivo

# Busca padrão regex no arquivo txt com regex padrão de telefone

leitura_regex = LerRegexEmArquivo('arquivos/base.txt', 'tel')

# Exporta para csv

leitura_regex.exportacao('csv')
