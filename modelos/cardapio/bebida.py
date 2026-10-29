from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho: str) -> None:
        super().__init__(nome, preco)
        self._tamanho = tamanho
    
    def __str__(self) -> str:
        """Return the beverage's information."""
        return f'{self._nome} - {self._preco} - {self._tamanho}'

    @property
    def tamanho(self) -> str:
        """Bebida size (read-only)."""
        return self._tamanho
    
    