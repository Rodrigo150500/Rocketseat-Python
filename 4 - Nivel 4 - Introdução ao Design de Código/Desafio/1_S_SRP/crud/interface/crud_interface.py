from abc import ABC, abstractmethod

class CRUD_Interface(ABC):
    @abstractmethod
    def create_task(self, task:str) -> None:
        pass

    @abstractmethod
    def update_task(self, task: str) -> None:
        pass

    @abstractmethod
    def read_task(self, task:str) -> None:
        pass