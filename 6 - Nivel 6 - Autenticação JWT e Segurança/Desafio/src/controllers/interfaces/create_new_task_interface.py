from abc import ABC, abstractmethod

class CreateNewTaskInterface(ABC):

    @abstractmethod
    def create(self, user_id: int, task_name: str, task_detail: str) -> dict:
        pass
