from src.models.settings.db_connecting_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.edit_balance_controller import EditBalanceController
from src.views.edit_balance_view import EditBalanceView

def edit_balance_composer():

    conn = db_connection_handler.get_connection()
    repository = UserRepository(conn)
    controller = EditBalanceController(repository)
    view = EditBalanceView(controller)

    return view