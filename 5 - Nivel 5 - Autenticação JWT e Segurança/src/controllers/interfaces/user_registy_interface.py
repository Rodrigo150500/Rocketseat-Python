from abc import ABC, abstractmethod

class UserRegistryInterface(ABC):
    def registry(self, username: str, password: str):
        pass