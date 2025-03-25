from .registry_user_view import RegistryUserView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class MockController:

    def registry(self, username, password):
        return {
            "data": "datas"
        }

def test_registry_user_view():

    http_request = HttpRequest(body={
        "username": "Rodrigo",
        "password": "ABC123"
    })

    controller = MockController()

    view = RegistryUserView(controller)

    response = view.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'response':{'data':'datas'}}
