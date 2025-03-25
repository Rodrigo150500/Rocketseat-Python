from src.models.interfaces.user_repository_interface import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from .interfaces.user_registy_interface import UserRegistryInterface

class UserRegistryController(UserRegistryInterface):
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.__repository = repository
        self.__password_handler = PasswordHandler()

    def registry(self, username: str, password: str):
        hashed_password = self.__encrypt_password(password)
        self.__registry_new_user(username, hashed_password)
        format_response = self.__format_response(username)
        return format_response


    def __encrypt_password(self, password: str) -> str:
        hashed_password = self.__password_handler.encrypt_password(password)
        return hashed_password

    def __registry_new_user(self, username: str, hashed_password: str) -> None:
        self.__repository.registry_user(username, hashed_password)

    def __format_response(self, username: str) -> dict:
        return {
            "data":{
                "type": "User",
                "count": 1,
                "username": username
            }
        }