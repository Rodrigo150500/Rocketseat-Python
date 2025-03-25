from src.controllers.interfaces.login_interface import LoginInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

from src.errors.error_types.http_bad_request import HttpBadRequest


class LoginView(ViewInterface):

    def __init__(self, controller: LoginInterface ) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        username = http_request.body['username']
        password = http_request.body['password']

        self.__validate_input(username, password)

        response = self.__controller.login(username, password)

        return HttpResponse(body={
            "response":response,
        }, status_code=200)



    def __validate_input(self, username: str, password: str):

        if (not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)):
            raise HttpBadRequest("Invalid Input")

