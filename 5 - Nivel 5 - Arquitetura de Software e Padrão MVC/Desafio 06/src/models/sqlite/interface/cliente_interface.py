from abc import ABC, abstractmethod

class ClienteInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, nome: str, valor_sacar: float) -> dict:
        pass

    @abstractmethod
    def realizar_extrato(self, nome: str) -> float:
        pass