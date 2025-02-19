from abc import ABC, abstractmethod

class ClienteInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, nome_pessoa: str, valor_sacar: float) -> dict:
        pass

    @abstractmethod
    def realizar_extrato(self, nome_pessoa: str) -> float:
        pass