from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.task import Task


class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> Task:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, task_id: UUID) -> Task | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        raise NotImplementedError
