from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    def registry_user(self, name: str, password: str) -> None:
        pass