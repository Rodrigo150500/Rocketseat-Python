from src.models.settings.db_connecting_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.user_registry_controller import UserRegistryController
from src.views.user_resgistry_view import UserResgistryView

def user_registry_composer():

    conn = db_connection_handler.get_connection()
    repository = UserRepository(conn)
    controller = UserRegistryController(repository)
    view = UserResgistryView(controller)

    return view