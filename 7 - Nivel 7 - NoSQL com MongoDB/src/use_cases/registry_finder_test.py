from .registry_finder import RegistryFinder
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class MockRepository:

    def select_by_object_id(self, order_id: str):
        return {
            "_id": "123"
        }



def test_registry_finder():
    
    repo = MockRepository()

    use_case = RegistryFinder(repo)

    http_request = HttpRequest(
        path_params={
            "order_id":"123"
        }
    )

    response = use_case.find(http_request)

    assert isinstance(response, HttpResponse)
    assert response.body == {
        "data":{
                    "count":1,
                    "type": "Order",
                    "operation": "search_order",
                    "attributes": {
                        "_id":"123"
                    }
                }
    }
