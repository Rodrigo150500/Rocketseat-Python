from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_criar_usuario_controller import PessoaFisicaCriarUsuarioController
from src.views.pessoa_fisica_criar_usuario_view import PessoaFisicaCriarUsuarioView
from src.models.sqlite.settings.connection import db_connection_handler



def pessoa_fisica_criar_usuario_composer():
    
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaCriarUsuarioController(model)
    view = PessoaFisicaCriarUsuarioView(controller)

    return view