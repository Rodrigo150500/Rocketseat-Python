from src.controllers.interfaces.login_creator_interface import LoginCreatorInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:

        username = request.body.get("username")
        password = request.body.get("password")

        self.__validate_input(username, password)

        response = self.__controller.creator(username, password)

        return HttpResponse({"data":response},status_code=200)

    def __validate_input(self, username: any, password: any) -> None:
        if(
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ): raise Exception('Invalid Input!')