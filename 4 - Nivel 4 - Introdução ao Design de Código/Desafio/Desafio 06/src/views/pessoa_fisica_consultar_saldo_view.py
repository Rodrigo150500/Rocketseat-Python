from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.pessoa_fisica_consultar_saldo_interface import PessoaFisicaConsultarSaldoInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.validators.pessoa_consultar_saldo_validator import pessoa_consultar_saldo_validator

class PessoaFisicaConsultarSaldoView(ViewInterface):

    def __init__(self, controller: PessoaFisicaConsultarSaldoInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_consultar_saldo_validator(http_request)
        
        nome = http_request.body["nome"]

        response = self.__controller.consulta_saldo(nome)

        return HttpResponse(body= response, status_code=200)

        




