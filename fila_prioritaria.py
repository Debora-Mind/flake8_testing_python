from fila_base import FilaBase
from contantes import FILA_PRIORITARIA


class FilaPrioritaria(FilaBase):

    def gera_senha(self) -> None:
        self.senha_atual = f"{FILA_PRIORITARIA}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Senha {cliente_atual}, dirija-se ao caixa {caixa}"
