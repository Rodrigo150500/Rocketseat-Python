from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.pessoa_juridica_listar_usuarios_interface import PessoaJuridicaListarUsuariosInterface


class PessoaJuridicaListarUsuariosView(ViewInterface):

    def __init__(self, controller : PessoaJuridicaListarUsuariosInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        response = self.__controller.listar_usuarios()

        return HttpResponse(body= response, status_code=200)
