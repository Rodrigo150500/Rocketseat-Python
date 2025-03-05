from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_listar_usuarios_controller import PessoaJuridicaListarUsuariosController
from src.views.pessoa_juridica_listar_usuarios_view import PessoaJuridicaListarUsuariosView

def pessoa_juridica_listar_usuarios_composer():

    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaListarUsuariosController(model)
    view = PessoaJuridicaListarUsuariosView(controller)

    return view