import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_resgistry_view import UserResgistryView 

class MockController:
    def registry(self, username, password):
        return {
            "alguma": "coisa"
        }

def test_handle_registry_user():

    body = {
        "username": "Rodrigo",
        "password": "abc123"
    }

    mock_controller = MockController()

    request = HttpRequest(body=body)

    view = UserResgistryView(mock_controller)

    response = view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'response': {'alguma': 'coisa'}}

def test_handle_user_registry_with_no_username():
    
    body = {
        "password": "senha123"
    }

    mock_controller = MockController()

    resquest = HttpRequest(body=body)

    view = UserResgistryView(mock_controller)

    with pytest.raises(Exception):
        view.handle(resquest)


def test_handle_user_registry_with_no_password():
    
    body = {
        "username": "Rodrigo"
        
    }

    mock_controller = MockController()

    resquest = HttpRequest(body=body)

    view = UserResgistryView(mock_controller)

    with pytest.raises(Exception):
        view.handle(resquest)

def test_handle_user_registry_with_password_not_string():
    
    body = {
        "username": "Rodrigo",
        "password": 123
    }

    mock_controller = MockController()

    resquest = HttpRequest(body=body)

    view = UserResgistryView(mock_controller)

    with pytest.raises(Exception):
        view.handle(resquest)

def test_handle_user_registry_with_username_not_string():
    
    body = {
        "username": 123,
        "password": "senha123"
    }

    mock_controller = MockController()

    resquest = HttpRequest(body=body)

    view = UserResgistryView(mock_controller)

    with pytest.raises(Exception):
        view.handle(resquest)