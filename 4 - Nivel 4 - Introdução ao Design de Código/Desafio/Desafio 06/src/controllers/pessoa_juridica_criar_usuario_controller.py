import re
from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from src.models.sqlite.interface.pessoa_juridica_atributos_interface import PessoaJuridicaAtributosInterface
from .interfaces.pessoa_juridica_criar_usuario_interface import PessoaJuridicaCriarUsuarioInterface

class PessoaJuridicaCriarUsuarioController(PessoaJuridicaCriarUsuarioInterface):

    def __init__(self, repository: PessoaInterface | ClienteInterface) -> None:
        self.__repository = repository
    
    def criar_usuario(self, user_info: PessoaJuridicaAtributosInterface) -> dict:
        
        nome_fantasia = user_info.nome_fantasia
        celular = user_info.celular

        self.__validate_name(nome_fantasia)
        self.__validate_celular(celular)

        self.__insert_user_in_db(user_info)

        formatted_response = self.__format_response(user_info)

        return formatted_response

    def __insert_user_in_db(self, user: PessoaJuridicaAtributosInterface):

        self.__repository.criar_usuario(user)

    def __validate_name(self, nome_fantasia: str) -> None:

        caracters_non_valid = re.compile(r"[^a-zA-Z ]")

        if caracters_non_valid.search(nome_fantasia):
            raise Exception("Caracteres inválidos")

    
    def __validate_celular(self, celular: str) -> None:

        caracter_non_valid = re.compile(r"[^1-9-()+ ]")

        if caracter_non_valid.search(celular):
            raise Exception("Caracteres inválidos")

    def __format_response(self, person_info: PessoaJuridicaAtributosInterface) -> dict:
        return {
            "data":{
                "type": "Pessoa Fisica",
                "count": 1,
                "operation": "Criar Usuario",
                "atributes": {"nome_fantasia": person_info.nome_fantasia, "idade": person_info.idade}
            }
        }