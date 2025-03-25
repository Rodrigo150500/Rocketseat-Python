from abc import ABC, abstractmethod

class PessoaFisicaSacarDinheiroInterface(ABC):

    @abstractmethod    
    def sacar(self, saque_info: dict) -> dict:
        pass