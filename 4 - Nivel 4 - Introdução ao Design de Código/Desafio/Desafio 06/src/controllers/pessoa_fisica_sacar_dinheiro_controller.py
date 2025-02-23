import re
from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from .interfaces.pessoa_fisica_sacar_dinheiro_controller_interface import PessoaFisicaSacarDinheiroInterface

class PessoaFisicaSacarDinheiroController(PessoaFisicaSacarDinheiroInterface):

    def __init__(self, repository: ClienteInterface | PessoaInterface ) -> None:
        
        self.__repository = repository

    
    def sacar(self, saque_info: dict) -> dict:

        nome = saque_info["nome"]
        valor = saque_info["saque"]

        self.__validar_nome(nome)

        saque = self.__sacar_dinheiro_in_db(nome, valor)

        formatted_response = self.__format_reponse(saque)

        return formatted_response


    def __validar_nome(self, nome: str) -> None:

        non_valid_caracters = re.compile(r"^[a-zA-Z ] + $")


        if non_valid_caracters.match(nome):
            raise Exception("Caracteres inválidos")
        
    
    def __sacar_dinheiro_in_db(self, nome: str, valor:float) -> dict:

        saque = self.__repository.sacar_dinheiro(nome, valor)

        if not saque:
            raise Exception("Pessoa não encontrada")
        
        return saque

    def __format_reponse(self, response: str) -> dict:

        return {
            "data":{
                "type": "Pessoa Fisica",
                "count": 1,
                "operation": "Saque",
                "response": response
            }
        }