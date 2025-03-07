from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

from src.controllers.interfaces.pessoa_juridica_consultar_saldo_interface import PessoaJuridicaConsultarSaldoInterface
from src.validators.pessoa_consultar_saldo_validator import pessoa_consultar_saldo_validator

class PessoaJuridicaConsultarSaldoView(ViewInterface):

    def __init__(self, controller: PessoaJuridicaConsultarSaldoInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        pessoa_consultar_saldo_validator(http_request)

        nome = http_request.body.get("nome")

        response = self.__controller.consulta_saldo(nome)

        return HttpResponse(body= response, status_code=200)
