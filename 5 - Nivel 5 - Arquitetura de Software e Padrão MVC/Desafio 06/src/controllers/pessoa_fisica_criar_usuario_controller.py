import re
from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from src.models.sqlite.interface.pessoa_fisica_atributos_interface import PessoaFisicaInterface
from .interfaces.pessoa_fisica_criar_usuario_interface import PessoaFisicaCriarUsuarioInterface
from src.errors.errors_types.http_bad_request import HttpBadRequest

class PessoaFisicaCriarUsuarioController(PessoaFisicaCriarUsuarioInterface):

    def __init__(self, pessoa_fisica_repository: ClienteInterface | PessoaInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository
        
    def criar(self, person_info: PessoaFisicaInterface) -> dict:

        nome_completo = person_info.nome_completo
        celular = person_info.celular

        self.__validate_name(nome_completo)
        self.__validate_celular(celular)
        self.__insert_into_db(person_info)

        formatted_response = self.__format_response(person_info)

        return formatted_response


    def __validate_name(self, nome_completo: str) -> None:

        caracters_non_valid = re.compile(r"[^a-zA-Z ]")

        if caracters_non_valid.search(nome_completo):
            raise HttpBadRequest("Caracteres inválidos")

    
    def __validate_celular(self, celular: str) -> None:

        caracter_non_valid = re.compile(r"[^1-9-()+ ]")

        if caracter_non_valid.search(celular):
            raise HttpBadRequest("Caracteres inválidos")

    def __insert_into_db(self, person_info: PessoaFisicaInterface) -> None:

        self.__pessoa_fisica_repository.criar_usuario(person_info)

    def __format_response(self, person_info: PessoaFisicaInterface) -> dict:
        return {
            "data":{
                "type": "Pessoa Fisica",
                "count": 1,
                "operation": "Criar Usuario",
                "atributes": {"nome": person_info.nome_completo, "idade": person_info.idade}
            }
        }
