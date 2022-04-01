from fila_base import FilaBase
from contantes import FILA_PRIORITARIA


class FilaPrioritaria(FilaBase):

    def gera_senha(self) -> None:
        self.senha_atual = f"{FILA_PRIORITARIA}{self.codigo}"

    def chama_cliente(self, caixa: int) -> None:
        cliente = self.verifica_cliente(FILA_PRIORITARIA)
        self.imprime_na_tela(cliente, caixa)
