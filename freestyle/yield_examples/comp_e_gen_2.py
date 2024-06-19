# Mas eu não poderia simplesmente carregar todos os valores em uma lista e iterá-los normalmente no for, igual eu sempre fiz?
# Você até pode, mas pense o seguinte: e se essa lista tiver 1 Milhão de itens e você continuar sem saber direito quanto tempo os cálculos vão demorar,
# você carregaria os 1 Milhão de itens na memória e deixaria lá até os cálculos terminarem?

# Vamos usar a função getsizeof() do sys para medir melhor essa diferença.
# Essa função retorna o tamanho em bytes gastos pelo objeto passado por parâmetro.
from sys import getsizeof

one_million = 10**6

list_compr = [x for x in range(one_million)]
print(getsizeof(list_compr))
# >> 8697464 (claro que ira variar o tempo)

list_gener = (x for x in range(one_million))
print(getsizeof(list_gener))
# >> 88

# Veja que uma lista com o range de 1 Milhão utiliza 8697464 de bytes, enquanto generator utiliza apenas 88 bytes.
# Dividindo um pelo outro (8697464/88), você chega em uma razão de mais de 98000 vezes!