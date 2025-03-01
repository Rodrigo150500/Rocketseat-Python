from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.edit_balance_interface import EditBalanceInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class EditBalanceView(ViewInterface):
    def __init__(self, controller: EditBalanceInterface) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest ) -> HttpResponse:

        userId = request.params.get("user_id")
        new_balance = request.body.get("new_balance")
        token_header_id = request.headers.get('uid')


        self.__validate_input(userId, new_balance, token_header_id)

        response = self.__controller.edit(userId, new_balance)

        return HttpResponse({'data': response}, status_code=200)
    def __validate_input(self, user_id: any, new_balance: float, token_header_id:any ) -> None:

        if(
            not user_id
            or not new_balance
            or not isinstance(new_balance, float)
            or not (int(token_header_id) != user_id)
        ): raise Exception("Invalid Input!")