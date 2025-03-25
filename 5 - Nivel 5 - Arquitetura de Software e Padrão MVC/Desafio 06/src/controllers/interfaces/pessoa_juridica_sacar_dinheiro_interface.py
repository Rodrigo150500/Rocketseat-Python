from abc import ABC, abstractmethod

class PessoaJuridicaSacarDinheiroInterface(ABC):

    @abstractmethod
    def sacar(self, saque_info: dict) -> dict:
        pass
