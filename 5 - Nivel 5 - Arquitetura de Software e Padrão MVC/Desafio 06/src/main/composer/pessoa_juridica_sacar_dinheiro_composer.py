from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_sacar_dinheiro_controller import PessoaJuridicaSacarDinheiroController
from src.views.pessoa_juridica_sacar_dinheiro_view import PessoaJuridicaSacarDinheiroView

def pessoa_juridica_sacar_dinheiro_composer():

    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaSacarDinheiroController(model)
    view = PessoaJuridicaSacarDinheiroView(controller)

    return view