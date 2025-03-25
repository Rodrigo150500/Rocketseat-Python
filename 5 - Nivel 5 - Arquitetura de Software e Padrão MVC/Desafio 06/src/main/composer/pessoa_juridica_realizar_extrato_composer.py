from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_realizar_extrato_controller import PessoaJuridicaRealizarExtratoController
from src.views.pessoa_juridica_realizar_extrato_view import PessoaJuridicaRealizarExtratoView

def pessoa_juridica_realizar_extrato():

    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaRealizarExtratoController(model)
    view = PessoaJuridicaRealizarExtratoView(controller)

    return view