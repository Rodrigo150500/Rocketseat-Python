from .list_all_tasks_by_user_id_controller import ListAllTasksByUserIdController

class MockRepository:

    def list_all_tasks_by_user_id(self, user_id):

        tasks = [(1, "15/03/2025 6:48:11", "Limpar quarto", "Arrumar a cama e mesa"),
                 (2, "15/03/2025 6:48:11", "Fazer almoço", "Preparar arroz, feijão e frango"),
                 (3, "15/03/2025 6:48:11", "Estudar python", "Realizar as aulas 1 e 2 de python")]

        return tasks

def test_list_all_tasks_by_user_id():

    mock_repository = MockRepository()

    controller = ListAllTasksByUserIdController(mock_repository)

    response = controller.list(1)

    expected_response = {
        "data":{
                "operation": "list tasks",                
                "user_id": 1,
                "tasks": ["Limpar quarto", "Fazer almoço", "Estudar python"],
                "tasks_count": 3                
            }
    }

    assert response == expected_response