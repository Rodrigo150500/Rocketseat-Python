from abc import ABC, abstractmethod

class PessoaJuridicaRealizarExtratoInterface(ABC):

    @abstractmethod
    def realizar_extrato(self, nome_pessoa: str) -> dict:
        pass
