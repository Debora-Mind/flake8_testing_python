from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

fila_normal = FabricaFila.pega_fila('normal')
fila_prioritaria = FabricaFila.pega_fila('prioritaria')

fila_normal.atualiza_fila()
fila_prioritaria.atualiza_fila()
fila_normal.atualiza_fila()

print(fila_normal.chama_cliente(10))
print(fila_normal.chama_cliente(2))
print(fila_prioritaria.chama_cliente(1))

print(fila_prioritaria.estatisticas(EstatisticaDetalhada(186, '20/02/2021')))
