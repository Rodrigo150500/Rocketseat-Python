from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_criar_usuario_controller import PessoaJuridicaCriarUsuarioController
from src.views.pessoa_juridica_criar_usuario_view import PessoaJuridicaCriarUsuarioView

def pessoa_juridica_criar_usuarios_composer():

    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaCriarUsuarioController(model)
    view = PessoaJuridicaCriarUsuarioView(controller)

    return view