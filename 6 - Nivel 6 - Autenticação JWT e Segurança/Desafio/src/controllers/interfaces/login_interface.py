from abc import ABC, abstractmethod

class LoginInterface(ABC):

    @abstractmethod
    def login(self, username: str, password: str) -> dict:
        pass
