import re
from src.models.sqlite.interface.cliente_interface import Cliente
from src.models.sqlite.interface.pessoa_interface import PessoaInterface

class PessoaFisicaSacarDinheiroController:

    def __init__(self, repository: Cliente | PessoaInterface ) -> None:
        
        self.__repository = repository

    
    def sacar(self, saque_info: dict) -> dict:

        nome = saque_info["nome_completo"]
        valor = saque_info["saque"]

        self.__validar_nome(nome)

        response = self.__repository.sacar_dinheiro(nome, valor)

        formatted_response = self.__format_reponse(response)

        return formatted_response


    def __validar_nome(self, nome: str) -> None:

        non_valid_caracters = re.compile(r"^[a-zA-Z ] + $")


        if non_valid_caracters.match(nome):
            raise Exception("Caracteres inválidos")
        

    def __format_reponse(self, response: str) -> dict:

        return {
            "data":{
                "type": "Pessoa Fisica",
                "count": 1,
                "operation": "Saque",
                "response": response
            }
        }