from abc import ABC, abstractmethod

class LoginCreatorInterface(ABC):

    def creator(self, username: str, password: str) -> dict:
        pass