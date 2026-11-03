import requests
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato

API_URL = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

def carregar_restaurantes_da_api() -> dict[str, Restaurante]:
    """Load restaurants and their menu items from the API."""
    try:
        response = requests.get(API_URL, timeout=10)
    except requests.exceptions.RequestException as erro:
        print(f'Não foi possível acessar a API: {erro}')
        return {}

    if response.status_code != 200:
        print(f'Erro ao carregar a API: {response.status_code}')
        return {}

    restaurantes_por_nome = {}
    for item in response.json():
        nome = item['Company']
        if nome not in restaurantes_por_nome:
            restaurantes_por_nome[nome] = Restaurante(nome, 'Sem categoria')
        prato = Prato(item['Item'], item['price'], item['description'])
        restaurantes_por_nome[nome].adicionar_no_cardapio(prato)
    return restaurantes_por_nome



#response = requests.get(API_URL)

#if response.status_code == 200:
#    dados_json = response.json()
#    for item in dados_json:
#        nome_do_restaurante = item['Company']
#        categoria_do_restaurante = item['Item']
#        Restaurante(nome_do_restaurante, categoria_do_restaurante)

#else:
#    print(f'O erro foi {response.status_code}')