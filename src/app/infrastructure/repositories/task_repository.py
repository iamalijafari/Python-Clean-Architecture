from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.repositories.task_repository import TaskRepository
from app.domain.task import Task
from app.infrastructure.database.models import TaskModel


class SqlAlchemyTaskRepository(TaskRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, task: Task) -> Task:
        model = self._session.get(TaskModel, task.id)
        if model is None:
            model = TaskModel(
                id=task.id,
                title=task.title,
                is_completed=task.is_completed,
            )
            self._session.add(model)
        else:
            model.title = task.title
            model.is_completed = task.is_completed

        self._session.commit()
        self._session.refresh(model)
        return self._to_domain(model)

    def get_by_id(self, task_id: UUID) -> Task | None:
        model = self._session.get(TaskModel, task_id)
        return self._to_domain(model) if model else None

    def list(self) -> list[Task]:
        models = self._session.scalars(select(TaskModel).order_by(TaskModel.title)).all()
        return [self._to_domain(model) for model in models]

    def delete(self, task_id: UUID) -> None:
        model = self._session.get(TaskModel, task_id)
        if model:
            self._session.delete(model)
            self._session.commit()

    @staticmethod
    def _to_domain(model: TaskModel) -> Task:
        task = Task(model.title, task_id=model.id)
        if model.is_completed:
            task.complete()
        return task
