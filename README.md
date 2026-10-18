# Python-Clean-Architecture

A minimal Python backend scaffold organized around Clean Architecture principles.

## Requirements

- Python 3.11 or newer
- `pip` and `venv`

## Set up a local environment

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project in editable mode with development tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run checks

Run the test suite:

```bash
python -m pytest
```

Check code style and imports:

```bash
ruff check .
ruff format --check .
```

To apply Ruff formatting:

```bash
ruff format .
```

The scaffold intentionally does not include a web framework, database driver, or AI provider SDK. Those choices should follow the actual project requirements.
