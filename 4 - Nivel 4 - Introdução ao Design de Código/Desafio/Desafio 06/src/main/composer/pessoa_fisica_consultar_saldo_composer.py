from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_consultar_saldo_controller import PessoaFisicaConsultarSaldoController
from src.views.pessoa_fisica_consultar_saldo_view import PessoaFisicaConsultarSaldoView
from src.models.sqlite.settings.connection import db_connection_handler

def pessoa_fisica_consultar_saldo_composer():

    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaConsultarSaldoController(model)
    view = PessoaFisicaConsultarSaldoView(controller)

    return view