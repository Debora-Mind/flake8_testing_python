import abc

from contantes import TAMANHO_MAXIMO_FILA, TAMANHO_MINIMO_FILA

class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_MAXIMO_FILA:
            self.codigo = TAMANHO_MINIMO_FILA
        else:
            self.codigo += 1

    def estatisticas(self, agencia: int, data: str, flag: str) -> dict:
        if flag != "detail":
            estatisticas = {f"{agencia} - {data}": len(self.clientes_atendidos)}

        else:
            estatisticas = {'agencia': agencia,
                            'data': data,
                            'clientes atendidos': self.clientes_atendidos,
                            'numero de clientes': len(self.clientes_atendidos)}

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
