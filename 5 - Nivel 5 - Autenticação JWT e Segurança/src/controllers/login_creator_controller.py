from src.models.interfaces.user_repository_interface import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler

class LoginCreatorController:

    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.__repository = repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()
    
    def creator(self, username: str, password: str) -> dict:
        user_verify = self.__verify_if_user_exists(username)
        userID = user_verify[0]
        hashed_password = user_verify[2]

        self.__check_password(password, hashed_password)

        token = self.__create_token(userID)

        return self.__format_response(token, username)


    def __verify_if_user_exists(self, username) -> tuple[int, str, str]:
        user = self.__repository.get_user_by_username(username)

        if not user: raise Exception ("User not found")

        return user


    def __check_password(self, password: str, hashed_password: str) -> None:
        password_validation = self.__password_handler.check_password(password, hashed_password)
        if password_validation == False: raise Exception("Wrong Password")

    def __create_token(self, userID: int) -> str:
        payload = {
            "user_id": userID
        }

        token = self.__jwt_handler.create_token(payload)
        return token

    def __format_response(self, token: str, username: str) -> dict:
        return{
            "acess": True,
            "username": username,
            "token": token
        }