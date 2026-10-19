from app.application.dto.task_dto import TaskDTO
from app.domain.repositories.task_repository import TaskRepository


class ListTasks:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def execute(self) -> list[TaskDTO]:
        return [TaskDTO.model_validate(task) for task in self._repository.list()]
