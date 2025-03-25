from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_sacar_dinheiro_controller import PessoaFisicaSacarDinheiroController
from src.views.pessoa_fisica_sacar_dinheiro_view import PessoaFisicaSacarDinheiroView
from src.models.sqlite.settings.connection import db_connection_handler

def pessoa_fisica_sacar_dinheiro_composer():

    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaSacarDinheiroController(model)
    view = PessoaFisicaSacarDinheiroView(controller)

    return view