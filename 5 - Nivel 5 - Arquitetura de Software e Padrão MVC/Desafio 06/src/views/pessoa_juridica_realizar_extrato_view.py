from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.pessoa_juridica_realizar_extrato_interface import PessoaJuridicaRealizarExtratoInterface


class PessoaJuridicaRealizarExtratoView(ViewInterface):

    def __init__(self, controller : PessoaJuridicaRealizarExtratoInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        nome = http_request.body.get("nome")

        response = self.__controller.realizar_extrato(nome)

        return HttpResponse(body= response, status_code=200)
