from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_consultar_saldo_controller import PessoaJuridicaConsultarSaldoController
from src.views.pessoa_juridica_consultar_saldo_view import PessoaJuridicaConsultarSaldoView

def pessoa_juridica_consultar_saldo_composer():

    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaConsultarSaldoController(model)
    view = PessoaJuridicaConsultarSaldoView(controller)

    return view