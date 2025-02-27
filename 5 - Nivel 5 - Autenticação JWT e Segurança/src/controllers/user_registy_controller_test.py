from src.controllers.user_registry_controller import UserRegistryController

class MockRepository:

    def __init__(self) -> None:
        self.registry_user_attributes = {}

    def registry_user(self, username:str, password: str) -> None:
        self.registry_user_attributes['username'] = username
        self.registry_user_attributes['password'] = password
    
def test_registry_user():

    repository = MockRepository()

    username = "Rodrigo"
    password = "Takara"

    controller = UserRegistry(repository)

    response = controller.registry(username, password)

    assert isinstance(response, dict)
    assert response['data']['type'] == 'User'
    assert repository.registry_user_attributes['username'] == username
    assert repository.registry_user_attributes['password'] is not None
    assert repository.registry_user_attributes['password'] != password

