from uuid import UUID

from app.application.dto.task_dto import TaskDTO
from app.domain.repositories.task_repository import TaskRepository


class GetTask:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def execute(self, task_id: UUID) -> TaskDTO | None:
        task = self._repository.get_by_id(task_id)
        return TaskDTO.model_validate(task) if task else None
