class Restaurante:
    def __init__(self, nome: str, categoria: str, ativo: bool = False) -> None:
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

