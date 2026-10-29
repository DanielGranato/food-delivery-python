class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str, ativo: bool = False) -> None:
        self._nome = nome
        self._categoria = categoria
        self._ativo = ativo
        Restaurante.restaurantes.append(self)

    @property
    def nome(self) -> str:
        """Restaurant name (read-only)."""
        return self._nome

    @property
    def ativo(self) -> bool:
        """Whether the restaurant is active (read-only)."""
        return self._ativo

    def alternar_estado(self) -> None:
        """Switch between active and inactive."""
        self._ativo = not self._ativo

    @classmethod
    def listar_restaurantes(cls) -> None:
        """Print every registered restaurant."""
        for restaurante in cls.restaurantes:
            ativo = 'Ativado' if restaurante._ativo else 'Desativado'
            print(f'- {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {ativo.ljust(20)}')
