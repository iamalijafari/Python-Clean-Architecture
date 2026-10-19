from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker
from testcontainers.postgres import PostgresContainer

import app.main as main_module
from app.api.dependencies import get_task_repository
from app.infrastructure.database.models import Base
from app.infrastructure.repositories.task_repository import SqlAlchemyTaskRepository


@pytest.fixture(scope="session")
def database_engine() -> Generator[Engine, None, None]:
    with PostgresContainer("postgres:17-alpine", driver="psycopg") as postgres:
        engine = create_engine(postgres.get_connection_url(), pool_pre_ping=True)
        Base.metadata.create_all(bind=engine)
        yield engine
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture
def client(
    database_engine: Engine,
    monkeypatch: pytest.MonkeyPatch,
) -> Generator[TestClient, None, None]:
    Base.metadata.drop_all(bind=database_engine)
    Base.metadata.create_all(bind=database_engine)
    monkeypatch.setattr(main_module, "engine", database_engine)

    test_session_factory = sessionmaker(
        bind=database_engine,
        autoflush=False,
        autocommit=False,
    )

    def override_task_repository() -> Generator[SqlAlchemyTaskRepository, None, None]:
        session: Session = test_session_factory()
        try:
            yield SqlAlchemyTaskRepository(session)
        finally:
            session.close()

    main_module.app.dependency_overrides[get_task_repository] = override_task_repository
    with TestClient(main_module.app) as test_client:
        yield test_client
    main_module.app.dependency_overrides.clear()
