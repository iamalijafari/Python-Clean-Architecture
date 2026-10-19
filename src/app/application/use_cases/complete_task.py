from uuid import UUID

from app.application.dto.task_dto import TaskDTO
from app.domain.repositories.task_repository import TaskRepository


class CompleteTask:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def execute(self, task_id: UUID) -> TaskDTO | None:
        task = self._repository.get_by_id(task_id)
        if task is None:
            return None

        task.complete()
        updated = self._repository.add(task)
        return TaskDTO.model_validate(updated)
