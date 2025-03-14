from abc import ABC, abstractmethod

class RegistryUserInterface(ABC):

    @abstractmethod
    def registry(self, username: str, password: str) -> dict:
        pass
