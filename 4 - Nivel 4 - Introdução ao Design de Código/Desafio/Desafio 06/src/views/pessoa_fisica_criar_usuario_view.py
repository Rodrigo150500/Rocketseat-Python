from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.pessoa_fisica_criar_usuario_interface import PessoaFisicaCriarUsuarioInterface 
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.models.sqlite.interface.pessoa_fisica_atributos_interface import PessoaFisicaInterface

class PessoaFisicaCriarUsuarioView(ViewInterface):

    def __init__(self, controller: PessoaFisicaCriarUsuarioInterface) -> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest, user: PessoaFisicaInterface) -> HttpResponse:

        new_user = PessoaFisicaInterface(
            nome_completo = http_request.body.get("nome_completo"),
            idade = http_request.body.get("idade"),
            categoria = http_request.body.get("categoria"),
            celular = http_request.body.get("celular"),
            email = http_request.body.get("email"),
            saldo = http_request.bool.get("saldo"),
            renda_mensal = http_request.body.get("renda_mensal")
        )

        response = self.__controller.criar(new_user)

        return HttpResponse(status_code= 201, body= response)

