from src.controllers.interfaces.pessoa_fisica_sacar_dinheiro_interface import PessoaFisicaSacarDinheiroInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PessoaFisicaSacarDinheiroView(ViewInterface):

    def __init__(self, controller: PessoaFisicaSacarDinheiroInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        user_info = http_request.body

        response = self.__controller.sacar(user_info)

        return HttpResponse(body= response, status_code=200)
