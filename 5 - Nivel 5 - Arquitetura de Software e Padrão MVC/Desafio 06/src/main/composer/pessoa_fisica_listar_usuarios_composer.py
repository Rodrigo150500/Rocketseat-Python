from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_listar_usuarios_controller import PessoaFisicaListarUsuariosController
from src.views.pessoa_fisica_listar_usuarios_view import PessoaFisicaListarUsuariosView
from src.models.sqlite.settings.connection import db_connection_handler


def pessoa_fisica_listar_usuarios_composer():

    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaListarUsuariosController(model)
    view = PessoaFisicaListarUsuariosView(controller)

    return view