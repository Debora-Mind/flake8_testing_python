from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from contantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA

Class = Union[FilaNormal, FilaPrioritaria]


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila: str) -> Class:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')
