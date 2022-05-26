from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


fila_teste = FabricaFila.pega_fila('prioritaria')
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chama_cliente(5))
print(fila_teste.estatistica(EstatisticaDetalhada('01/03/2021', 1030)))
print(fila_teste.estatistica(EstatisticaResumida('01/03/2021', 1030)))