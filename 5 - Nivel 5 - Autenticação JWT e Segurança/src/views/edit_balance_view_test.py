import pytest
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .edit_balance_view import EditBalanceView

class MockController:
    def edit(self, userID, new_balance):
        return  {
            "type": "User",
            "count": 1,
            "new balance": new_balance
        }


def test_handle_edit_balance():

    params = {
        "user_id": 5
    }
    body = {
        "new_balance": 15.55
    }

    request = HttpRequest(body=body, params=params)

    mock_controller = MockController()

    view = EditBalanceView(mock_controller)

    response = view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {
        "data":{
            "type": "User",
            "count": 1,
            "new balance": body["new_balance"]
        }
    }

def test_handle_edit_balance_with_no_user_id():
    
    body = {
        "new_balance": 15.55
    }
    params = {}
    request = HttpRequest(body=body, params=params)
    
    mock_controller = MockController()
    
    view = EditBalanceView(mock_controller)
    
    with pytest.raises(Exception):
        view.handle(request)

def test_handle_edit_balance_with_no_balance():
    
    body = {
    }
    params = {
        "user_id": 5
    }
    request = HttpRequest(body=body, params=params)
    
    mock_controller = MockController()
    
    view = EditBalanceView(mock_controller)
    
    with pytest.raises(Exception):
        view.handle(request)


def test_handle_edit_balance_with_new_balance_not_float():

    params = {
        "user_id": 5
    }
    body = {
        "new_balance": 3
    }

    request = HttpRequest(body=body, params=params)

    mock_controller = MockController()

    view = EditBalanceView(mock_controller)

    with pytest.raises(Exception):
        view.handle(request)

    