import pytest
from .registry_user_controller import RegistryUserController

class MockRepository:

    def registry_user(self, username: str, password: str):
        pass

    def get_user_by_username(self ,username: str):
        return False

class MockRepositoryError:

    def registry_user(self, username: str, password: str):
        pass

    def get_user_by_username(self ,username: str):
        return True

def test_registry_user_controller():

    repo = MockRepository()

    controller = RegistryUserController(repo)

    username = "Rodrigo"
    password = "ABC123"
    
    response = controller.registry(username, password)

    expected_response = {
            "data":{
                "operation": "registry user",
                "count": 1,
                "username": username
            }
        }
    
    assert response == expected_response

def test_registry_user_controller_with_error():

    repo = MockRepositoryError()

    controller = RegistryUserController(repo)

    username = "Rodrigo"
    password = "ABC123"

    with pytest.raises(Exception):
        controller.registry(username, password)

 