from src.models.settings.conection import db_conection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_controller import LoginController
from src.views.login_view import LoginView

def login_composer() -> LoginView:

    conn = db_conection_handler.get_connection()

    model = UserRepository(conn)
    controller = LoginController(model)
    view = LoginView(controller)

    return view

