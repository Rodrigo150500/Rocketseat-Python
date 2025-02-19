import re
from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface


class PessoaFisicaConsultarSaldoController:
    def __init__(self, repository: ClienteInterface|PessoaInterface) -> None:
        self.__repository = repository

    def consulta_saldo(self, nome_pessoa: str) -> dict:

        saldo = self.__get_saldo(nome_pessoa)

        formatted_response = self.__format_reponse(saldo)

        return formatted_response

    def __get_saldo(self, nome_pessoa: str) -> float:

        saldo = self.__repository.consultar_saldo(nome_pessoa)

        return saldo

    def __format_reponse(self, saldo: float) -> dict:
        return {
            "data":{
                "type":"Pessoa Fisica",
                "count": 1,
                "operation": "consulta saque",
                "response": saldo
            }
        }
