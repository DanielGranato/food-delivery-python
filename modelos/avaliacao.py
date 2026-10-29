class Avaliacao:
    def __init__(self, cliente: str, nota: int) -> None:
        self._cliente = cliente
        self._nota = nota

    @property
    def nota(self) -> int:
        """Rating given by the client (read-only)."""
        return self._nota

    def __str__(self) -> str:
        return f'Cliente: {self._cliente}, Nota: {self._nota}'