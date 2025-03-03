from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.pessoa_fisica_listar_usuarios_interface import PessoaFisicaListarUsuariosInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class PessoaFisicaListarUsuariosView(ViewInterface):

    def __init__(self, controller: PessoaFisicaListarUsuariosInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        response = self.__controller.listar_usuarios()

        return HttpResponse(body = response, status_code=200)