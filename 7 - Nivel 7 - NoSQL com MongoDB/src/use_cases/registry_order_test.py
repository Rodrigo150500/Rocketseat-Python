import pytest
from .registry_order import RegistryOrder
from src.main.http_types.http_request import HttpRequest

class MockRepository:

    def insert_document(self, document: dict):
        pass

class MockRepositoryError:

    def insert_document(self, document: dict):
        raise Exception("Erro aqui")

def test_insert_document():
    
    repo = MockRepository()

    use_case = RegistryOrder(repo)

    order = HttpRequest(
        body={
            "data":{
                "name": "joazinho",
                "address":"rua do limao",
                "cupom": False,
                "items":[
                    {"item":"Refrigerante", "quantidade": 2},
                    {"item": "Pizza", "quantidade": 3}
                ]
            }
        }
    )

    response = use_case.registry(order)
    
    assert response.body == {
        "data":{
                "type": "Order",
                "count":1,
                "registry": True,
                "operation": "insert_document"
            }
        }
    assert response.status_code == 201
    
def test_with_error():

    repo = MockRepositoryError()

    use_case = RegistryOrder(repo)

    order = HttpRequest(
        body={
            "data":{
                "name": "joazinho",
                "address":"rua do limao",
                "cupom": False,
                "items":[
                    {"item":"Refrigerante", "quantidade": 2},
                    {"item": "Pizza", "quantidade": 3}
                ]
            }
        }
    )
    
    response = use_case.registry(order)
    assert "errors" in response.body
    assert str(response.body["errors"][0]["detail"]) == "Erro aqui"
    assert response.status_code == 500