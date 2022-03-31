from typing import Union, List, Dict


class EstatisticaResumida:
    def __init__(self, agencia: int, data: str) -> None:
        self.agencia = agencia
        self.data = data

    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, int] = (
            {f"{self.agencia} - {self.data}": len(clientes_atendidos)})

        return estatistica
