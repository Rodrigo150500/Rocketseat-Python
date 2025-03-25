import pytest
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .login_creator_view import LoginCreatorView

class MockController:
    def creator(self, username, password):
        return{
            "acess": True,
            "username": username,
            "token": "15364as6ds4ad8asd3as1a"
        }

def test_handle_login_creator():

    body = {
        "username": "Rodrigo",
        "password": "ABC132"
    }

    request = HttpRequest(body=body)
    
    mock_controller = MockController()

    view = LoginCreatorView(mock_controller)

    response = view.handle(request)

    assert isinstance(response, HttpResponse)

    assert response.body ==  {
            'data':{
                    "acess": True,
                    "username": body['username'],
                    "token": "15364as6ds4ad8asd3as1a"
            }
        }

def test_handle_login_creator_with_no_username():
    
    body = {
        "password": "ABC132"
    }

    request = HttpRequest(body=body)
    
    mock_controller = MockController()

    view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception):
        view.handle(request)

    

def test_handle_login_creator_with_no_password():
    body = {
        "username": "Rodrigo"
        
    }

    request = HttpRequest(body=body)
    
    mock_controller = MockController()

    view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception):
        view.handle(request)

def test_handle_login_creator_with_username_not_string():
    body = {
        "username": 123,
        "password": "ABC132"
    }

    request = HttpRequest(body=body)
    
    mock_controller = MockController()

    view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception):
        view.handle(request)

def test_handle_login_creator_with_password_not_string():
    body = {
        "username": "Rodrigo",
        "password": 123
    }

    request = HttpRequest(body=body)
    
    mock_controller = MockController()

    view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception):
        view.handle(request)