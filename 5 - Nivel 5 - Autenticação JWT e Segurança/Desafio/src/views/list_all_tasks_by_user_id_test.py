import pytest
from .list_all_tasks_by_user_id_view import ListAllTasksByUserIdView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class MockController:

    def list(self, user_id):

        task_list = ["Limpar quarto", "Varrer o chão", "Arrumar impressora"]

        return{
            "data":{
                "operation": "list tasks",                
                "user_id": user_id,
                "tasks": task_list,
                "tasks_count": len(task_list)                
            }
        }



def test_list_all_tasks_by_user_id():

    mock_controller = MockController()

    view = ListAllTasksByUserIdView(mock_controller)

    http_request = HttpRequest(params={
        "user_id": "1"
    })

    response = view.handle(http_request)

    task_list = ["Limpar quarto", "Varrer o chão", "Arrumar impressora"]

    expected_response = { 
        "data":{
                "operation": "list tasks",                
                "user_id": "1",
                "tasks": task_list,
                "tasks_count": len(task_list)                
            }
        }

    assert isinstance(response, HttpResponse)
    assert response.body == expected_response

def test_list_all_tasks_by_user_id_with_error():

    mock_controller = MockController()

    view = ListAllTasksByUserIdView(mock_controller)

    http_request = HttpRequest(params={
        "user_id": 1
    })

    with pytest.raises(Exception):
        view.handle(http_request)

 