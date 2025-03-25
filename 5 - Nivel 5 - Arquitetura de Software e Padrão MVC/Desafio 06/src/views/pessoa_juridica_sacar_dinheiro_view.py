from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.pessoa_juridica_sacar_dinheiro_interface import PessoaJuridicaSacarDinheiroInterface


class PessoaJuridicaSacarDinheiroView(ViewInterface):

    def __init__(self, controller : PessoaJuridicaSacarDinheiroInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        request = http_request.body

        response = self.__controller.sacar(request)

        return HttpResponse(body= response, status_code=200)
