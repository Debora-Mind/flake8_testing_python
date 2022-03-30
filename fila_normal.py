from fila_base import FilaBase
from contantes import FILA_NORMAL

class FilaNormal(FilaBase):

    def gera_senha(self) -> None:
        self.senha_atual = f"{FILA_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Senha {cliente_atual}, dirija-se ao caixa {caixa}"
