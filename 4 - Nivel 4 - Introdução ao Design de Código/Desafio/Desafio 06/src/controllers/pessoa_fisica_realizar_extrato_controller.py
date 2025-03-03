from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from src.models.sqlite.interface.cliente_interface import ClienteInterface
from .interfaces.pessoa_fisica_realizar_extrato_interface import PessoaFisicaRealizarExtratoInterface

class PessoaFisicaRealizarExtratoController(PessoaFisicaRealizarExtratoInterface):
    def __init__(self, repository: PessoaInterface | ClienteInterface) -> None:
        self.__repository = repository

    
    def realizar_extrato(self, nome_pessoa: str) -> dict:

        get_extrato_in_db = self.__get_extrato_in_db(nome_pessoa)

        formated_response = self.__formated_response(get_extrato_in_db)

        return formated_response

    def __get_extrato_in_db(self, nome_pessoa: str) -> dict:

        extrato = self.__repository.realizar_extrato(nome_pessoa)

        if not extrato:
            raise Exception("Pessoa não encontrada")
        
        return extrato

    def __formated_response(self, extrato: dict) -> dict:

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
    

