# food-delivery-python

Learning project: a food delivery app in Python to practice functions, object-oriented programming and API consumption. Fictional, for study only. Do not use real restaurant brands or real customer data.

## How to work with me
- Talk to me in Portuguese (Brazil). Code, comments, docstrings, README and commit messages in English.
- I am learning Python: before a big change, explain briefly what you will do and why, and name the concept used (e.g. "this is inheritance", "this is a pure function"). Keep explanations short.
- Prefer small, reviewable steps: one concept or feature at a time. Do not rewrite working code just to make it "better".
- Ask before adding any dependency that is not listed here.
- When I ask for a solution, show the simple version first. Mention the more advanced option in one line only.

## Project history
This is a single project that grows with my Alura courses. It started as a terminal app where restaurants were dictionaries inside a list. I am now refactoring it to use classes, following the object-oriented programming course (class `Restaurante` in `modelos/restaurante.py`). Keep using classes and objects; do not go back to dictionaries. Follow the course's lessons and naming (Portuguese names for functions, variables and classes, as in the course).

## Stack
- Python 3.12 or newer, virtual environment in `.venv/`
- `requests` for API calls
- No test tools yet. I will add pytest when the course reaches testing.
- Terminal (CLI) app: text menus with `input()` and `print()`. No GUI and no web framework.
- TODO: which API is consumed

## Structure
Follow the folder structure and file names from the Alura course I am currently taking. Do not create extra folders or layers on your own. If I ask where something should go, suggest the simplest option and explain why in one or two sentences. We can reorganize later when the project grows.

## Concepts this project must practice
- Functions: parameters, return values, default arguments, pure functions, small and single-purpose.
- OOP: classes, `__init__`, attributes and methods, encapsulation, inheritance and polymorphism where it makes sense (e.g. different kinds of menu items), `__str__` / `__repr__`.
- API consumption: `requests.get`, status codes, timeouts, JSON parsing, error handling (`try/except`), no crash on network failure.
- Terminal input: validate what the user types (empty text, letters instead of numbers, out-of-range choices) and ask again instead of crashing.
- Bonus: type hints, docstrings, basic tests.

## Style rules
- Follow PEP 8 (snake_case for functions and variables, PascalCase for classes).
- Add type hints to function signatures and a one-line docstring to each public function or class.
- Handle errors with specific exceptions, never a bare `except:`.
- No hard-coded secrets, tokens or API keys. Read them from environment variables (`.env` is in `.gitignore`).
- No global mutable state.

## Rules
- Never commit `.venv/`, `__pycache__/`, `.env` or any secret.
- After a change, tell me how to run the app and what to check by hand. Do not install testing tools unless I ask.
- Keep `README.md` in sync when features or commands change.

## Commands
- `python -m venv .venv` and `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`)
- `pip install -r requirements.txt`
- `python main.py`

## How to work with me
- I am following the Alura "Python back end" career path. Match the course's style and examples when possible, and tell me when you do something differently from the lesson.
