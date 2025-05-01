from src.models.repository.interfaces.order_repository_interface import OrderRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.validators.registry_order_update_validator import registry_order_update_validator
from src.errors.erro_handler import error_handler

class RegistryUpdater:
    
    def __init__(self, order_repository: OrderRepositoryInterface) -> None:
        self.__order_repository = order_repository
    
    def update(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.path_params["order_id"]
            body = http_request.body

            self.__validate_body(body)

            self.__update_registry(order_id, body)

            return self.__format_response(order_id)
        
        except Exception as exception:
            return error_handler(exception)
    
    def __validate_body(self, body: dict) -> None:

        registry_order_update_validator(body)

    def __update_registry(self, order_id: str, body: dict) -> None:
        update_field = body["data"]
        self.__order_repository.edit_registry(order_id, update_field)


    def __format_response(self, order_id: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data":{
                    "order_id": order_id,
                    "type": "Order",
                    "count": 1,
                    "operation": "update_registry"
                }
            },
            status_code= 200
        )