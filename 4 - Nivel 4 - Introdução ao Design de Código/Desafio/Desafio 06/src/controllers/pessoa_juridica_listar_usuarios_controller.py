from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaListarUsuarios:
    def __init__(self, repository: ClienteInterface | PessoaInterface) -> None:
        self.__repository = repository

    
    def listar_usuarios(self) -> dict:

        users = self.__get_users()

        formatted_response = self.__formated_response(users)

        return formatted_response
    
    def __get_users(self) -> list[PessoaJuridicaTable]:

        users = self.__repository.listar_usuarios()

        return users

    def __formated_response(self, users: list[PessoaJuridicaTable]) -> dict:

        formatted_users= []

        for user in users:
            formatted_users.append({"nome_fantasia": user.nome_fantasia, "idade": user.idade})

        return {
            "data":{
                "type": "Pessoa Juridica",
                "count": len(users),
                "operation": "listar usuarios",
                "atributes": formatted_users
            }
        }