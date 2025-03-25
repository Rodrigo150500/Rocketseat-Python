from src.models.settings.conection import db_conection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.create_new_task_controller import CreateNewTaskController
from src.views.create_new_taks_view import CreateNewTaskView

def create_new_task_composer() -> CreateNewTaskView:

    conn = db_conection_handler.get_connection()
    model = UserRepository(conn)
    controller = CreateNewTaskController(model)
    view = CreateNewTaskView(controller)

    return view