from src.controllers.interfaces.registry_user_interface import RegistryUserInterface
from .interfaces.registry_user_interface import RegistryUserInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class RegistryUserView(RegistryUserInterface):

    def __init__(self, controller: RegistryUserInterface) -> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        username = http_request.body["username"]
        password = http_request.body["password"]

        self.__validate_input(username, password)

        response = self.__controller.registry(username, password)

        return HttpResponse(body={
            "response": response
        }, status_code = 201)


    def __validate_input(self, username: str, password: str) -> None:

        if (not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
            ): raise Exception("Invalid Input")




    

