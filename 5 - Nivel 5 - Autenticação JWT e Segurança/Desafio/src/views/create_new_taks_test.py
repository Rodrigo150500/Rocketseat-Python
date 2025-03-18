import pytest
from .create_new_taks_view import CreateNewTaskView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class MockController:

    def create(self, user_id: int, task_name: str, task_detail: str) -> dict:
        return {
            "data":{
                "operation":"create task",
                "task_name": task_name,
                "user_id": user_id
            }
        }

def test_create_new_task():
    
    mock_controller = MockController()

    view = CreateNewTaskView(mock_controller)

    http_request = HttpRequest(
        body={
            "task_name": "Limpar quarto",
            "task_detail": "varrer e passar pano"
        },
        params={
            "user_id": 1
        },
        header={
            "uid": 1
        }
    )

    response = view.handle(http_request)

    assert isinstance(response, HttpResponse)

    expected_response = {   
            "data":{
                "operation":"create task",
                "task_name": "Limpar quarto",
                "user_id": 1
            }
        }
        
    assert response.body["response"] == expected_response

def test_create_new_task_with_error():
    
    mock_controller = MockController()

    view = CreateNewTaskView(mock_controller)

    http_request = HttpRequest(
        body={
            "task_name": "Limpar quarto",
            "task_detail": ""
        },
        params={
            "user_id": 2
        },
        header={
            "uid": 2
        }
    )

    with pytest.raises(Exception):
        view.handle(http_request)

