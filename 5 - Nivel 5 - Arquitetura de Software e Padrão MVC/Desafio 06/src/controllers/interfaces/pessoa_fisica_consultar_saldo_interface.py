from abc import ABC, abstractmethod

class PessoaFisicaConsultarSaldoInterface(ABC):

    @abstractmethod
    def consulta_saldo(self, nome_pessoa: str) -> dict:
        pass
