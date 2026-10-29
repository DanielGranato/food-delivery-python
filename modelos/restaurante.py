from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str, ativo: bool = False) -> None:
        self._nome = nome
        self._categoria = categoria
        self._ativo = ativo
        self._avaliacoes = []
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
            print(f'- {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {ativo.ljust(20)}')

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
