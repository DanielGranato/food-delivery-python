import json
from modelos.restaurante import Restaurante

def salvar_restaurantes_em_arquivo(restaurantes: dict[str, Restaurante]) -> None:
    """Save restaurants to a JSON file."""
    dados = {nome: restaurante.para_dicionario() for nome, restaurante in restaurantes.items()}
    conteudo = json.dumps(dados, indent=4, ensure_ascii=False)
    try:
        with open('restaurantes.json', 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    except OSError as erro:
        print(f'Erro ao salvar restaurantes: {erro}')

def carregar_restaurantes_do_arquivo() -> dict[str, Restaurante]:
    """Load restaurants from a JSON file."""
    try:
        with open('restaurantes.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except (OSError, json.JSONDecodeError) as erro:
        print(f'Erro ao carregar restaurantes: {erro}')
        return {}
    return {nome: Restaurante(**campos) for nome, campos in dados.items()}
