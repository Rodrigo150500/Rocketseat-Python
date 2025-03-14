from src.drivers.password_handler import PasswordHandler
from src.models.repositories.interfaces.user_repository_interface import UserRepositoryInterface
from .interfaces.registry_user_interface import RegistryUserInterface

class RegistryUserController(RegistryUserInterface):
    
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.password_handler = PasswordHandler()
        self.repository = repository        
    
    def registry(self, username: str, password: str) -> dict:

        self.__verify_if_user_already_exists(username)

        hashed_password = self.__encrypt_password(password)

        self.repository.registry_user(username, hashed_password)

        response = self.__format_response(username)

        return response

    def __verify_if_user_already_exists(self, username: str) -> None:
        
        user_exists = self.repository.get_user_by_username(username)

        if user_exists:
            raise Exception("User already exists!")

    def __encrypt_password(self, password: str) -> str:
        hashed_password = self.password_handler.encrypt_password(password)

        return hashed_password

        
    def __format_response(self, username: str) -> dict:
        return {
            "data":{
                "operation": "registry user",
                "count": 1,
                "username": username
            }
        }