from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    def registry_user(self, name: str, password: str) -> None:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> tuple[int, str, str]:
        pass

    @abstractmethod
    def list_all_tasks_by_user_id(self, user_id: int) -> tuple[int, str, str, str]:
        pass

    @abstractmethod
    def create_new_task(self, user_id: int, task_name: str, task_detail: str ) -> None:
        pass

