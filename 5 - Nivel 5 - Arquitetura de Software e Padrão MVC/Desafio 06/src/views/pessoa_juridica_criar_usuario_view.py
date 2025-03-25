from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.pessoa_juridica_criar_usuario_interface import PessoaJuridicaCriarUsuarioInterface
from src.models.sqlite.interface.pessoa_juridica_atributos_interface import PessoaJuridicaAtributosInterface
from src.validators.pessoa_juridica_criar_usuario_validator import pessoa_juridica_criar_usuario_validator

class PessoaJuridicaCriarUsuarioView(ViewInterface):

    def __init__(self, controller : PessoaJuridicaCriarUsuarioInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        pessoa_juridica_criar_usuario_validator(http_request)
        
        new_user = PessoaJuridicaAtributosInterface(
            faturamento= http_request.body.get("faturamento"),
            idade = http_request.body.get("idade"),
            nome_fantasia= http_request.body.get("nome_fantasia"),
            celular = http_request.body.get("celular"),
            email_corporativo= http_request.body.get("email_corporativo"),
            categoria= http_request.body.get("categoria"),
            saldo = http_request.body.get("saldo")
            )

        response = self.__controller.criar_usuario(new_user)

        return HttpResponse(body= response, status_code= 201)