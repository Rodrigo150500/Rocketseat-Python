from .registry_updater import RegistryUpdater
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class MockRepository:

    def edit_registry(self, order_id, update_fields):
        pass

def test_registry_update():

    repo = MockRepository()

    use_case = RegistryUpdater(repo)

    http_request = HttpRequest(
        path_params={
            "order_id": "123"
        },
        body={
            "data":{
                "name":"Rodrigo",
                "address":"Rua dos Patinhos",
                "cupom": False
            }
        }

    )

    response = use_case.update(http_request)

    assert isinstance(response, HttpResponse)
    assert response.body == {
         "data":{
                    "order_id": "123",
                    "type": "Order",
                    "count": 1,
                    "operation": "update_registry"
                }
    }
    assert response.status_code == 201