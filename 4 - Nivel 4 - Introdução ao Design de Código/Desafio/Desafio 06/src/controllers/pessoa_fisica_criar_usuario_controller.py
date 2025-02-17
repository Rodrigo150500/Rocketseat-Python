import re
from src.models.sqlite.interface.cliente_interface import Cliente
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from src.models.sqlite.interface.pessoa_fisica_atributos_interface import PessoaFisicaInterface
from .interfaces.pessoa_fisica_criar_usuario_controller_interface import PessoaFisicaCriarUsuarioInterface


class PessoaFisicaCriarUsuarioController(PessoaFisicaCriarUsuarioInterface):

    def __init__(self, pessoa_fisica_repository: Cliente | PessoaInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository
        
    def criar(self, person_info: dict) -> dict:

        renda_mensal = person_info["renda_mensal"]
        idade = person_info["idade"]
        nome_completo = person_info["nome_completo"]
        celular = person_info["celular"]
        email = person_info["email"]
        categoria = person_info["categoria"]
        saldo = person_info["saldo"]

        self.__validate_name(nome_completo)
        self.__validate_celular(celular)
        self.__insert_into_db(person_info)

        formatted_response = self.__format_response(person_info)

        return formatted_response


    def __validate_name(self, nome_completo: str) -> None:

        caracters_non_valid = re.compile(r"[^a-zA-Z ]")

        if caracters_non_valid.search(nome_completo):
            raise Exception("Caracteres inválidos")

    
    def __validate_celular(self, celular: str) -> None:

        caracter_non_valid = re.compile(r"[^1-9-()+ ]")

        if caracter_non_valid.search(celular):
            raise Exception("Caracteres inválidos")

    def __insert_into_db(self, person_info: dict) -> None:

        user_data = PessoaFisicaInterface(
            renda_mensal = person_info["renda_mensal"],
            idade = person_info["idade"],
            nome_completo = person_info["nome_completo"],
            celular = person_info["celular"],
            email = person_info["email"],
            categoria = person_info["categoria"],
            saldo = person_info["saldo"]
        )

        self.__pessoa_fisica_repository.criar_usuario(user_data)

    def __format_response(self, person_info: dict) -> dict:
        return {
            "data":{
                "type": "Pessoa Fisica",
                "count": 1,
                "operation": "Criar Usuario",
                "atributes": person_info
            }
        }
