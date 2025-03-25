from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.pessoa_fisica_realizar_extrato_interface import PessoaFisicaRealizarExtratoInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.validators.pessoa_realizar_extrato_validator import pessoa_realizar_extrato_validator

class PessoaFisicaRealizarExtratoView(ViewInterface):

    def __init__(self, controller: PessoaFisicaRealizarExtratoInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        pessoa_realizar_extrato_validator(http_request)

        nome = http_request.body.get("nome")

        response = self.__controller.realizar_extrato(nome)

        return HttpResponse(body = response, status_code = 200)