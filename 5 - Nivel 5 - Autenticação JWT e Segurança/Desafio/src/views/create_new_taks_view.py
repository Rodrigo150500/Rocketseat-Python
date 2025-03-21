from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.create_new_task_interface import CreateNewTaskInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

from src.errors.error_types.http_bad_request import HttpBadRequest

class CreateNewTaskView(ViewInterface):

    def __init__(self, controller: CreateNewTaskInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        user_id = http_request.params["user_id"]
        task_name = http_request.body["task_name"]
        task_detail = http_request.body["task_detail"]
        header_uid = http_request.header["uid"]

        self.__validate_input(user_id, task_name, task_detail, header_uid)

        response = self.__controller.create(user_id, task_name, task_detail)

        return HttpResponse(body={
            "response": response
        }, status_code= 201)

    def __validate_input(self, user_id: int, task_name: str, task_detail: str, header_uid: int):
        
        if (not user_id
            or not task_name
            or not task_detail
            or not header_uid
            or user_id != header_uid):
            raise HttpBadRequest("Invalid Input")