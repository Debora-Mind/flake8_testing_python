class FilaPrioritaria:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def gera_senha(self) -> None:
        self.senha_atual = f"FP{self.codigo}"

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Senha {cliente_atual}, dirija-se ao caixa {caixa}"

    def estatisticas(self, agencia: int, data: str, flag: str) -> dict:
        if flag != "detail":
            estatisticas = {f"{agencia} - {data}": len(self.clientes_atendidos)}

        else:
            estatisticas = {'agencia': agencia,
                            'data': data,
                            'clientes atendidos': FilaPrioritaria.clientes_atendidos,
                            'numero de clientes': len(FilaPrioritaria.clientes_atendidos)}

        return estatisticas
