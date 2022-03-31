import abc
from typing import List, Dict, Union

from contantes import TAMANHO_MAXIMO_FILA, TAMANHO_MINIMO_FILA
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_MAXIMO_FILA:
            self.codigo = TAMANHO_MINIMO_FILA
        else:
            self.codigo += 1

    def estatisticas(self, agencia: int, data: str, retorna_estatistica) -> dict:
        estatistica = retorna_estatistica(agencia, data)
        return estatistica.roda_estatistica(self.clientes_atendidos)

    @abc.abstractmethod
    def gera_senha(self) -> None:
        ...

    def adiciona_cliente_fila(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha()
        self.adiciona_cliente_fila()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...
