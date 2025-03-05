from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_realizar_extrato_controller import PessoaFisicaRealizarExtratoController
from src.views.pessoa_fisica_realizar_extrato_view import PessoaFisicaRealizarExtratoView
from src.models.sqlite.settings.connection import db_connection_handler

def pessoa_fisica_realizar_extrato_composer():

    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaRealizarExtratoController(model)
    view = PessoaFisicaRealizarExtratoView(controller)

    return view