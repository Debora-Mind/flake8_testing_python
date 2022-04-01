from fila_base import FilaBase
from contantes import FILA_NORMAL


class FilaNormal(FilaBase):

    def gera_senha(self) -> None:
        self.senha_atual = f"{FILA_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa: int) -> None:
        cliente = self.verifica_cliente(FILA_NORMAL)
        self.imprime_na_tela(cliente, caixa)
