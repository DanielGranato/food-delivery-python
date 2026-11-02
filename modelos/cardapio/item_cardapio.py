from abc import ABC, abstractmethod

class ItemCardapio(ABC):
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

    @abstractmethod
    def __str__(self) -> str:
        """Return the item's information."""
        return f'{self._nome} - {self._preco}'

    @abstractmethod
    def aplicar_desconto(self) -> float:
        """Apply a discount to the item."""
        return self._preco