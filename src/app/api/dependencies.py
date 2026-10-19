from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_db_session
from app.infrastructure.repositories.task_repository import SqlAlchemyTaskRepository


def get_task_repository(
    session: Session = Depends(get_db_session),
) -> Generator[SqlAlchemyTaskRepository, None, None]:
    yield SqlAlchemyTaskRepository(session)
