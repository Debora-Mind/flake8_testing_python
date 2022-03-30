from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

# fila = FilaNormal()
fila_prioritaria = FilaPrioritaria()

# fila.atualiza_fila()
# fila.atualiza_fila()
# fila.atualiza_fila()
#
# print(fila.chama_cliente(3))
# print(fila.chama_cliente(3))
# print(fila.chama_cliente(3))

fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()

print(fila_prioritaria.chama_cliente(10))
print(fila_prioritaria.chama_cliente(5))
print(fila_prioritaria.chama_cliente(2))

print(fila_prioritaria.estatisticas(154, '10/10/2022', 'detail'))
