from src.models.settings.db_connecting_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_creator_controller import LoginCreatorController
from src.views.login_creator_view import LoginCreatorView

def login_creator_composer():
    conn = db_connection_handler.get_connection()
    repository = UserRepository(conn)
    controller = LoginCreatorController(repository)
    view = LoginCreatorView(controller)

    return view