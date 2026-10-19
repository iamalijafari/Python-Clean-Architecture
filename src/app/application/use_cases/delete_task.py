from uuid import UUID

from app.domain.repositories.task_repository import TaskRepository


class DeleteTask:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def execute(self, task_id: UUID) -> bool:
        if self._repository.get_by_id(task_id) is None:
            return False
        self._repository.delete(task_id)
        return True
