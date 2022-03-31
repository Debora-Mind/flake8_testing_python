from typing import Union, List, Dict


class EstatisticaDetalhada:
    def __init__(self, agencia: int, data: str) -> None:
        self.agencia = agencia
        self.data = data

    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, Union[str, int, List[str]]] = (
            {'agencia': self.agencia,
             'data': self.data,
             'clientes atendidos': clientes_atendidos,
             'numero de clientes': len(clientes_atendidos)})

        return estatistica
