from .create_new_task_controller import CreateNewTaskController

class MockRepository:

    def create_new_task(self, user_id, task_name, task_detail):
        pass



def test_create_task():

    repository = MockRepository()

    controller = CreateNewTaskController(repository)

    user_id = 1
    task_name = "Limpar cozinha"
    task_detail = "Limpar o chão, mesas e cadeiras"

    response = controller.create(user_id, task_name, task_detail)

    expected_response = {
        "data":{
            "operation":"create task",
            "task_name": task_name,
            "user_id": user_id
        }
    }

    assert response == expected_response