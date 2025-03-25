from abc import ABC, abstractmethod

class ListAllTasksByUserIdInterface(ABC):

    @abstractmethod
    def list(self, user_id: int) -> dict:
        pass