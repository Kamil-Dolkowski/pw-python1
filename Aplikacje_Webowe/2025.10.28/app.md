# Poetry

```bash
# Instalacja
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/u334531/.local/bin:$PATH"

poetry --version

poetry new backend

cd frontend/
poetry init

cd backend
poetry add requests
```

### Flake8

mozliwości, style, na co zwraca uwagę, kody błędów

```bash
# Dodanie zależności
poetry add --group dev pytest black flake8

# Konkretna wersja
poetry add --group dev "pytest==8.4.1"
poetry add --group dev "pytest>=8.2.1,<8.4.0"

# Własny moduł
poetry add --group dev mymodule

# Odinstalowywanie zależności (w głównym projekcie)
poetry remove flake8

# Odinstalowywanie zależności (w danej grupie)
poetry remove --group dev black

# Aktualizowanie zalezności
poetry update
poetry update pytest
poetry show --outdated

poetry install
```

```
requires-python = ">=3.12"
requires-python = "^3.12"
requires-python = "~3.12.0-9" # tylko patche
requires-python = "=3.*"
```

```bash
poetry env info --path

poetry shell
poetry env activate
poetry env list

poetry run pytest

poetry config --list

poetry export -f requirements.txt --output requirements.txt --without-hashes

# Cashowanie
poetry cache list
poetry cache clear PyPI --all

poetry run start

# Podnoszenie wersji
poetry version patch
poetry version minor
poetry version major
poetry version 1.2.3
```

# Pre-commit

- nie pozwala na commita, jeśli nie spełnia określonych warunków
- wczesne wykrywanie błędów, zanim kod trafi do repo
- spójność kodu (yaml checker, end of file fixer)

