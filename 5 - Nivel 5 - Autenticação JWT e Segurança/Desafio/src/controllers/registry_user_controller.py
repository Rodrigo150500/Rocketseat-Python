import re
from src.drivers.password_handler import PasswordHandler
from src.models.repositories.interfaces.user_repository_interface import UserRepositoryInterface
from .interfaces.registry_user_interface import RegistryUserInterface

from src.errors.error_types.http_bad_request import HttpBadRequest

class RegistryUserController(RegistryUserInterface):
    
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.password_handler = PasswordHandler()
        self.repository = repository        
    
    def registry(self, username: str, password: str) -> dict:

        self.__validate_username(username)

        self.__verify_if_user_already_exists(username)

        hashed_password = self.__encrypt_password(password)

        self.repository.registry_user(username, hashed_password)

        response = self.__format_response(username)

        return response

    def __validate_username(self, username: str) -> None:

        valid_characters = re.compile(r"^[a-zA-Z-09 ]+$")

        if valid_characters.match(username):
            raise HttpBadRequest("Caracter Inválido")


    def __verify_if_user_already_exists(self, username: str) -> None:
        
        user_exists = self.repository.get_user_by_username(username)

        if user_exists:
            raise HttpBadRequest("User already exists!")

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