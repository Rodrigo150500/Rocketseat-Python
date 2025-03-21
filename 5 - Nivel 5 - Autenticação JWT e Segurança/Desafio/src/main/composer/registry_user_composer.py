from src.models.settings.conection import db_conection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.registry_user_controller import RegistryUserController
from src.views.registry_user_view import RegistryUserView


def registry_user_composer() -> RegistryUserView:

    conn = db_conection_handler.get_connection()

    model = UserRepository(conn)
    controller = RegistryUserController(model)
    view = RegistryUserView(controller)

    return view
