from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.pessoa_juridica_criar_usuario_interface import PessoaJuridicaCriarUsuarioInterface
from src.models.sqlite.interface.pessoa_juridica_atributos_interface import PessoaJuridicaAtributosInterface

class PessoaJuridicaCriarUsuarioView(ViewInterface):

    def __init__(self, controller : PessoaJuridicaCriarUsuarioInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        new_user = PessoaJuridicaAtributosInterface(
            faturamento= htttp_request.body.get("faturamento"),
            idade = htttp_request.body.get("idade"),
            nome_fantasia= htttp_request.body.get("nome_fantasia"),
            celular = htttp_request.body.get("celular"),
            email_corporativo= htttp_request.body.get("email_corporativo"),
            categoria= htttp_request.body.get("categoria"),
            saldo = htttp_request.body.get("saldo")
            )

        response = self.__controller.criar_usuario(new_user)

        return HttpResponse(body= response, status_code= 201)