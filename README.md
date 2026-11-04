# food-delivery-python

> Python food delivery app: functions, OOP and API consumption.

A learning project built to practice core Python topics: functions, object-oriented programming and consuming a web API. It is a **terminal (command line) app** for study purposes; no real orders or payments are involved.

## What it does

- Loads restaurants and their menu items from a public API (`requests`).
- Lists the registered restaurants with category, average rating and status (active or inactive).
- Registers new restaurants and switches a restaurant between active and inactive.
- Saves the restaurants to `restaurantes.json` when you exit, and loads that file on the next run (the API is only used when there is no saved file).
- Handles network and file errors without crashing.

The menu text is in Portuguese:

```text
Sabor Express

1. Cadastrar restaurante
2. Listar restaurante
3. Alterar estado do restaurante
4. Sair

Escolha uma opção: _
```

## Requirements

- Python 3.12 or newer
- Windows (the screen is cleared with `cls`)

## Getting started

```bash
git clone https://github.com/DanielGranato/food-delivery-python.git
cd food-delivery-python
```

**1. Create the virtual environment** (once):

```bash
python -m venv venv
```

**2. Activate it** (every time you open a new terminal):

```bash
source venv/Scripts/activate     # Git Bash
.\venv\Scripts\Activate.ps1      # PowerShell
venv\Scripts\activate            # CMD
```

The terminal prompt shows `(venv)` when it is active.

**3. Install the dependencies:**

```bash
pip install -r requirements.txt
```

**4. Run the app:**

```bash
python app.py
```

Choose option `4` (Sair) to exit and save the restaurants. To start over from the API, delete `restaurantes.json`.

## Project structure

```
app.py                       entry point and terminal menu
modelos/
  restaurante.py             Restaurante class (also keeps the list of all restaurants)
  avaliacao.py               Avaliacao class (a customer rating)
  cardapio/
    item_cardapio.py         ItemCardapio, abstract base class
    prato.py                 Prato, a dish (inherits from ItemCardapio)
    bebida.py                Bebida, a drink (inherits from ItemCardapio)
services/
  api_restaurantes.py        loads restaurants and menu items from the API
  arquivos.py                saves and loads restaurantes.json
requirements.txt             dependencies
```

## Concepts practiced

| Topic | Where to look |
|---|---|
| Functions and terminal menu | `app.py` |
| Classes, attributes, properties | `modelos/restaurante.py`, `modelos/avaliacao.py` |
| Inheritance, abstract classes, polymorphism | `modelos/cardapio/` |
| API consumption (`requests`, timeout, status codes, errors) | `services/api_restaurantes.py` |
| Reading and writing JSON files | `services/arquivos.py` |

## Tech stack

- Python 3.12+
- `requests` (HTTP)

## Status

- [x] Project setup
- [x] Models (OOP)
- [x] API client
- [x] Save and load restaurants
- [ ] Save menu items and ratings
- [ ] Order flow
- [ ] Tests

## Credits and notes

- Data from the course API: <https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json>. It contains real brand names; the project is not affiliated with any of them.
- Fictional project for study.

## Author

Made by **Daniel Granato** · [GitHub](https://github.com/DanielGranato)
