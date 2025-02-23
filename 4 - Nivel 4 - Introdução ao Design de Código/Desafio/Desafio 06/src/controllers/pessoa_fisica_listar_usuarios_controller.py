from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from .interfaces.pessoa_fisica_listar_usuarios_controller_test_interface import PessoaFisicaListarUsuariosInterface

class PessoaFisicaListarUsuariosController(PessoaFisicaListarUsuariosInterface):
    def __init__(self, repository: ClienteInterface | PessoaInterface) -> None:
        self.__repository = repository

    def listar_usuarios(self) -> dict:

        users = self.__get_users()

        formated_response = self.__formated_response(users)

        return formated_response

    def __get_users(self) -> list[PessoaFisicaTable]:

        users = self.__repository.listar_usuarios()

        return users

    def __formated_response(self, users: list[PessoaFisicaTable]) -> dict:

        formatted_users = []

        for user in users:
            formatted_users.append({"nome_completo": user.nome_completo, "idade": user.idade })

        return {
            "data":{
                "type": "Pessoa Fisica",
                "count": len(users),
                "operation": "listar usuarios",
                "atributes": formatted_users
            }
        }