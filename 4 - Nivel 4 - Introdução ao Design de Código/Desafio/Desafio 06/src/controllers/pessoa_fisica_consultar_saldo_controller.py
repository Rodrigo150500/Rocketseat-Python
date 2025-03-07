from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from .interfaces.pessoa_fisica_consultar_saldo_interface import PessoaFisicaConsultarSaldoInterface

class PessoaFisicaConsultarSaldoController(PessoaFisicaConsultarSaldoInterface):
    def __init__(self, repository: ClienteInterface|PessoaInterface) -> None:
        self.__repository = repository

    def consulta_saldo(self, nome_pessoa: str) -> dict:

        saldo = self.__get_saldo(nome_pessoa)

        formatted_response = self.__format_response(saldo)

        return formatted_response

    def __get_saldo(self, nome_pessoa: str) -> float:

        saldo = self.__repository.consultar_saldo(nome_pessoa)

        return saldo

    def __format_response(self, saldo: float) -> dict:
        return {
            "data":{
                "type":"Pessoa Fisica",
                "count": 1,
                "operation": "consulta saldo",
                "response": saldo
            }
        }
