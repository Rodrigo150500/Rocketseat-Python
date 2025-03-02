from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface

class PessoaJuridicaRealizarExtratoController:
    def __init__(self, repository: ClienteInterface | PessoaInterface) -> None:
        self.__repository = repository
    
    def realizar_extrato(self, nome_pessoa: str) -> dict:

        get_extrato_in_db = self.__repository.realizar_extrato(nome_pessoa)

        formated_response = self.__formatted_response(get_extrato_in_db)

        return formated_response
    
    def __formatted_response(self, extrato: dict) -> dict:
        return {
            "data":{
                "type": "Pessoa Fisica",
                "count": 1,
                "operation": "realizar extrato",
                "atributes": {
                    "Nome": extrato["Nome"],
                    "Saldo": extrato['Saldo'],
                    "Categoria": extrato["Categoria"]

                }
            }
        }