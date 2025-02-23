from abc import ABC, abstractmethod

class PessoaFisicaRealizarExtratoInterface(ABC):

    @abstractmethod
    def realizar_extrato(self, nome_pessoa: str) -> dict:
        pass
