class Restaurante:
    def __init__(self, nome: str, categoria: str, ativo: bool = False) -> None:
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

restaurante_1 = Restaurante('Restaurante 1', 'Categoria 1', True)
restaurante_2 = Restaurante('Restaurante 2', 'Categoria 2', False)

restaurantes = [restaurante_1, restaurante_2]

