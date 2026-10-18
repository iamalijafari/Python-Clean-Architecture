from uuid import UUID, uuid4


class Task:
    """A task in the domain model."""

    def __init__(self, title: str, task_id: UUID | None = None) -> None:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")

        self.id = task_id or uuid4()
        self.title = title.strip()
        self.is_completed = False
