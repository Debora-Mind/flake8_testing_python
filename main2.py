# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila

# fila_normal = FilaNormal()
# fila_prioritaria = FilaPrioritaria()
fila_normal = FabricaFila.pega_fila('normal')
fila_prioritaria = FabricaFila.pega_fila('prioritaria')

fila_normal.atualiza_fila()
fila_prioritaria.atualiza_fila()
fila_normal.atualiza_fila()

print(fila_normal.chama_cliente(10))
print(fila_normal.chama_cliente(2))
print(fila_prioritaria.chama_cliente(1))

print(fila_prioritaria.estatisticas(154, '10/10/2022', 'detail'))
