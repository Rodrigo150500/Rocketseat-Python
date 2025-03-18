import pytest
from .login_view import LoginView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.drivers.jwt_handler import JwtHandler



class MockController:

    def login(self, username, password):

        jwt_handler = JwtHandler()

        body = {
            "user_id": 1
        }

        token = jwt_handler.create_token(body)


        return {
                "data": {
                "access": True,
                "username": username,
                "token": token
                }
             }

def test_login():


    mock_controller = MockController()

    view = LoginView(mock_controller)

    http_request = HttpRequest(body={
        "username": "Rodrigo",
        "password": "abc123"
    })

    response = view.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.body["response"]["data"]["access"] == True
    assert response.body["response"]["data"]["token"] is not None

def test_login_error():

    mock_controller = MockController()

    view = LoginView(mock_controller)

    http_request = HttpRequest(body={
        "username": "Rodrigo",
        "password": 123
    })

    with pytest.raises(Exception):
        view.handle(http_request)




    


    

