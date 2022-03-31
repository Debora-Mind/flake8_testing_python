import abc
from typing import List, Dict, Union

from contantes import TAMANHO_MAXIMO_FILA, TAMANHO_MINIMO_FILA


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

    def estatisticas(self, agencia: int, data: str, flag: str) -> dict:
        estatisticas: Dict[str, Union[str, int, List[str]]] = {}
        if flag == "detail":
            estatisticas['agencia'] = agencia
            estatisticas['data'] = data
            estatisticas['clientes atendidos'] = self.clientes_atendidos
            estatisticas['numero de clientes'] = len(self.clientes_atendidos)

        else:
            estatisticas[f"{agencia} - {data}"] = len(self.clientes_atendidos)

        return estatisticas

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
