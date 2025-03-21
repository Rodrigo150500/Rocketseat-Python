from src.models.settings.conection import db_conection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.list_all_tasks_by_user_id_controller import ListAllTasksByUserIdController
from src.views.list_all_tasks_by_user_id_view import ListAllTasksByUserIdView

def list_all_tasks_by_user_id_composer() -> ListAllTasksByUserIdView:

    conn = db_conection_handler.get_connection()
    model = UserRepository(conn)
    controller = ListAllTasksByUserIdController(model)
    view = ListAllTasksByUserIdView(controller)

    return view