from fastapi import FastAPI, Query
from services.api_restaurantes import carregar_restaurantes_da_api

app = FastAPI()

# Loaded once when the server starts, not on every request.
dados_restaurantes = carregar_restaurantes_da_api()

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)) -> dict[str, dict]:
    """Return the restaurants as JSON, optionally filtered by name."""
    # If the query has a name filter, keep only the matches; each restaurant becomes a dict with para_dicionario().
    if restaurante:
        return {
            nome: obj.para_dicionario()
            for nome, obj in dados_restaurantes.items()
            if restaurante.lower() in nome.lower()
        }

    return {nome: obj.para_dicionario() for nome, obj in dados_restaurantes.items()}

@app.get('/')
def inicio() -> dict[str, str]:
    """Return a welcome message pointing to the API docs."""
    return {'mensagem': 'API de restaurantes. Veja /docs'}