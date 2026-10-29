class ItemCardapio:
    def __init__(self, nome: str, preco: float) -> None:
        self._nome = nome
        self._preco = preco

    @property
    def nome(self) -> str:
        """Item name (read-only)."""
        return self._nome

    @property
    def preco(self) -> float:
        """Item price (read-only)."""
        return self._preco

