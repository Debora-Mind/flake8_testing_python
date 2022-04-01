import abc
from typing import List, Dict, Union

from contantes import TAMANHO_MAXIMO_FILA, TAMANHO_MINIMO_FILA
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

Class = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    @abc.abstractmethod
    def gera_senha(self) -> None:
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> None:
        ...

    @staticmethod
    def imprime_na_tela(cliente: str, caixa: int) -> None:
        if cliente:
            print(f"Senha {cliente}, dirija-se ao caixa {caixa}")

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_MAXIMO_FILA:
            self.codigo = TAMANHO_MINIMO_FILA
        else:
            self.codigo += 1

    def adiciona_cliente_fila(self) -> None:
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha()
        self.adiciona_cliente_fila()

    def verifica_cliente(self, tipo_fila: str) -> str:
        contador = 0
        while contador < len(self.fila):
            if tipo_fila in self.fila[contador]:
                cliente_atual = self.fila.pop(contador)
                self.clientes_atendidos.append(cliente_atual)
                return cliente_atual
            contador += 1
        return ''

    def estatisticas(self, retorna_estatistica: Class) -> Dict[str, Class]:
        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
