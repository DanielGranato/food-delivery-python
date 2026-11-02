from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str, ativo: bool = False) -> None:
        self._nome = nome
        self._categoria = categoria
        self._ativo = ativo
        self._avaliacoes = []
        self._cardapio = []
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
            media = str(restaurante.media_avaliacoes) if restaurante._avaliacoes else 'Sem avaliações'
            print(f'- {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {media.ljust(20)} | {ativo.ljust(20)}')

    def receber_avaliacao(self, cliente: str, nota: int) -> None:
        """Add an evaluation to the restaurant."""
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)
        print(f'Avaliação do cliente {cliente} adicionada com sucesso')

    @property
    def media_avaliacoes(self) -> float:
        """Calculate the average of the restaurant's evaluations."""
        if not self._avaliacoes:
            return 0
        soma_das_avaliacoes = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        quantidade_de_avaliacoes = len(self._avaliacoes)
        media = round(soma_das_avaliacoes / quantidade_de_avaliacoes, 1)
        return media

    #def adicionar_bebida(self, bebida: Bebida) -> None:
      #  """Add a beverage to the restaurant."""
      #  self._bebidas.append(bebida)

    #def adicionar_prato(self, prato: Prato) -> None:
      #  """Add a dish to the restaurant."""
      #  self._pratos.append(prato)

    #refactor

    @property
    def cardapio(self) -> list[ItemCardapio]:
        """Restaurant menu items (read-only)."""
        return self._cardapio

    def adicionar_no_cardapio(self, item: ItemCardapio) -> None:
        """Add an item to the restaurant's menu."""
        self._cardapio.append(item)

    def exibir_cardapio(self) -> None:
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            print(f'{i}. {item.nome.ljust(20)} | R$ {item.preco:.2f}')

    