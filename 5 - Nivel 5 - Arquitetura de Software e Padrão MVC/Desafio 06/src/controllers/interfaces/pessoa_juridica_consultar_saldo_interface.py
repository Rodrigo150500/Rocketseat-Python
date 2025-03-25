from abc import ABC, abstractmethod

class PessoaJuridicaConsultarSaldoInterface(ABC):

    @abstractmethod
    def consulta_saldo(self, nome_fantasia: str) -> dict:
        pass
