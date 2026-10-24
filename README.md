# food-delivery-python

> Python food delivery app: functions, OOP and API consumption.

A learning project built to practice core Python topics: functions, object-oriented programming and consuming a web API. It is a **terminal (command line) app** for study purposes; no real restaurants, orders or payments are involved.

<!-- Add a screenshot or a terminal recording (GIF) here -->

## Example

```text
=== Food Delivery ===
1. List restaurants
2. Build an order
3. Exit
Choose an option: _
```

<!-- Replace with a real output of your app. -->

## Requirements

Python 3.12 or newer. Works on Windows, macOS and Linux.

## What it does

TODO: describe in 3 or 4 bullets, for example:

- Lists restaurants and their menus (data from an API).
- Lets the user build an order and calculates the total.
- Handles errors (network failure, invalid input) without crashing.

## Concepts practiced

| Topic | Where to look |
|---|---|
| Functions | `app/utils/` |
| Terminal menus and input validation | `app/cli/` |
| Classes and OOP | `app/models/` |
| Business logic | `app/services/` |
| API consumption | `app/api/` |
| Tests | `tests/` |

## Tech stack

- Python 3.12+
- `requests` (HTTP)
- `pytest` (tests)

## Getting started

```bash
git clone https://github.com/DanielGranato/food-delivery-python.git
cd food-delivery-python
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Run the tests:

```bash
pytest
```

## Project structure

```
main.py        entry point
app/
  cli/         menus and terminal input/output
  models/      Restaurant, MenuItem, Customer, Order
  services/    business logic
  api/         API client
  utils/       helper functions
tests/
```

## Status

- [ ] Project setup
- [ ] Models (OOP)
- [ ] API client
- [ ] Order flow
- [ ] Tests

## Credits and notes

- TODO: name and link of the API used.
- Fictional project for study. Not affiliated with any real brand.

## Author

Made by **Daniel Granato** · [GitHub](https://github.com/DanielGranato)
