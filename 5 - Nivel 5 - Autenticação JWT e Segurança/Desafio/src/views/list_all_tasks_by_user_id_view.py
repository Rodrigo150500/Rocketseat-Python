from src.controllers.interfaces.list_all_tasks_by_user_id_interface import ListAllTasksByUserIdInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class ListAllTasksByUserIdView(ViewInterface):

    def __init__(self, controller: ListAllTasksByUserIdInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        user_id = http_request.params['user_id']

        self.__validate_input(user_id)

        response = self.__controller.list(user_id)

        return HttpResponse(body=response, status_code=200)


    def __validate_input(self, user_id: str) -> None:

        if (not user_id
            or isinstance(user_id, int)):
            raise Exception("Invalid Input")
