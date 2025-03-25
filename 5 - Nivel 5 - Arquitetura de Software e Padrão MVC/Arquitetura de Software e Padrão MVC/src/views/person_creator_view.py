from src.views.interfaces.view_interface import ViewInterface
from src.controller.interfaces.person_creator_controller import PersonCreatorControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.validators.person_creator_validator import person_creator_validator

class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
