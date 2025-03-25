from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from .interfaces.pessoa_juridica_consultar_saldo_interface import PessoaJuridicaConsultarSaldoInterface


class PessoaJuridicaConsultarSaldoController(PessoaJuridicaConsultarSaldoInterface):
    def __init__(self, repository: ClienteInterface | PessoaInterface ) -> None:
        self.__repository = repository

    def consulta_saldo(self, nome_fantasia: str) -> dict:

        saldo = self.__get_saldo(nome_fantasia)

        formatted_response = self.__format_response(saldo)

        return formatted_response

    def __get_saldo(self, nome_fantasia: str) -> float:

        saldo = self.__repository.consultar_saldo(nome_fantasia)

        return saldo

    def __format_response(self, saldo: float) -> dict:

        return {
            "data":{
                "type": "Pessoa Juridica",
                "count": 1,
                "operation": "consulta saldo",
                "response": saldo
            }
        }