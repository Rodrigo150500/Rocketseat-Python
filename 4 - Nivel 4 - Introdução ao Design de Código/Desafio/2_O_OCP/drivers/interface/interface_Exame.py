from abc import ABC, abstractmethod

class InterfaceExame(ABC):

    @abstractmethod
    def verificarExame(self):
        pass

    @abstractmethod
    def aprovarExame(self):
        pass