import re
from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface


class PessoaJuridicaSacarDinheiroController:
    def __init__(self, repository: ClienteInterface | PessoaInterface ) -> None:
        
        self.__repository = repository

    def sacar(self, saque_info: dict) -> dict:

        nome_fantasia = saque_info["nome"]
        valor = saque_info["saque"]

        self.__validar_nome_fantasia(nome_fantasia)

        saque = self.__sacar_dinheiro_in_db(nome_fantasia, valor)

        formatted_response = self.__format_response(saque)
        
        return formatted_response

    def __validar_nome_fantasia(self, nome_fantasia: str) -> None:

        non_caracters_valid = re.compile(r"^[a-zA-Z ] + $")

        if non_caracters_valid.match(nome_fantasia):
            raise Exception("Caracteres Invalidos")

    def __sacar_dinheiro_in_db(self, nome_fantasia: str, valor: float) -> dict:

        saque = self.__repository.sacar_dinheiro(nome_fantasia, valor)

        if not saque:
            raise Exception("Pessoa não encontrada")

        return saque

    def __format_response(self, response: dict) -> dict:
        return {
            "data":{
                "type": "Pessoa Juridica",
                "count": 1,
                "operation": "Saque",
                "response": response
            }
        }