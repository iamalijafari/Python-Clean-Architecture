# Python-Clean-Architecture

An educational FastAPI backend organized around Clean Architecture principles.

## Requirements

- Python 3.11 or newer for local development
- Docker Desktop or Docker Engine with the Docker Compose plugin

## Run with Docker Compose

Build the API image and start the API and PostgreSQL services:

```bash
docker compose up --build
```

The API is available at:

- Health check: http://localhost:8000/health
- Interactive API docs: http://localhost:8000/docs

Stop the services:

```bash
docker compose down
```

To stop the services and also delete the persisted PostgreSQL data volume, use this destructive command only when you intentionally want to reset the local database:

```bash
docker compose down --volumes
```

Compose configures the API to connect to the PostgreSQL service using the `DATABASE_URL` environment variable. PostgreSQL data is stored in the named `postgres_data` volume.

## Database layer

The project uses SQLAlchemy 2.x as its ORM (Object-Relational Mapper) and Psycopg 3 as the PostgreSQL driver. SQLAlchemy maps Python model classes to database tables and provides the database query/session API; Psycopg handles the PostgreSQL wire-protocol connection.

## Run locally without Docker

Create and activate a virtual environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project and development tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Set `DATABASE_URL` to a PostgreSQL connection string before starting the API locally. The default configuration points to `localhost:5432`.

## Run checks

```bash
python -m pytest
ruff check .
ruff format --check .
```

To apply Ruff formatting:

```bash
ruff format .
```
