from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler
from src.models.repositories.interfaces.user_repository_interface import UserRepositoryInterface
from .interfaces.login_interface import LoginInterface

class LoginController(LoginInterface):
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.jwt_handler = JwtHandler()
        self.password_hanler = PasswordHandler()
        self.__repository = repository
    
    def login(self, username: str, password: str) -> dict:
        
        user_info = self.__get_user_info(username)

        user_id = user_info[0]
        hashed_password = user_info[2]

        self.__validating_password(password, hashed_password)

        token = self.__create_token(user_id)

        formatted_response = self.__format_response(token, username)

        return formatted_response

                


    def __get_user_info(self, username: str) -> tuple[int, str, str]: #return id, username, password

        user = self.__repository.get_user_by_username(username)

        if not user:
            raise Exception("Usuário não encontrado")
        
        return user
    
    def __validating_password(self, password: str, hashed_password: str) -> None:
        
        check_password = self.password_hanler.check_password(password, hashed_password) 

        if not check_password:
            raise Exception("Invalid password!")
    
    def __create_token(self, user_id: int) -> str:

        body = {
            "user_id": user_id
        }

        token = self.jwt_handler.create_token(body)

        return token
        
    def __format_response(self, token: str, username: str) -> dict:
        return {
            "data": {
                "access": True,
                "username": username,
                "token": token
            }
        }

