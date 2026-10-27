class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str, ativo: bool = False) -> None:
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    @classmethod
    def listar_restaurantes(cls) -> None:
        """Print every registered restaurant."""
        for restaurante in cls.restaurantes:
            ativo = 'ativado' if restaurante.ativo else 'desativado'
            print(f'- {restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {ativo.ljust(20)}')
