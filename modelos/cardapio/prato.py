from modelos.cardapio.item_cardapio import ItemCardapio

class Prato (ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str) -> None:
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self) -> str:
        """Return the dish's information."""
        return f'{self._nome} - {self._preco} - {self._descricao}'  

    @property
    def descricao(self) -> str:
        """Prato description (read-only)."""
        return self._descricao
    

