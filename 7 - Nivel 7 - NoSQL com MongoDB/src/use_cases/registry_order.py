from datetime import datetime
from src.models.repository.interfaces.order_repository_interface import OrderRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class RegistryOrder:

    def __init__(self, order_repository: OrderRepositoryInterface):
        self.__order_repository = order_repository

    def registry(self, http_request: HttpRequest) -> HttpResponse:

        try:

            body = http_request.body

            new_order = self.__format_new_order(body)

            self.__registry_order(new_order)

            return self.__format_response()
        
        except Exception as exception:

            return HttpResponse(body={
                "Error": exception
            }, status_code=400)
    
    def __format_new_order(self, body: dict) -> dict:

        new_order = body["data"]

        new_order = {**new_order, "created_at": datetime.now()}

        return new_order
    
    def __registry_order(self, new_order: dict) -> None:

        self.__order_repository.insert_document(new_order)

    def __format_response(self) -> HttpResponse:

        return HttpResponse(body={
            "data":{
                "type": "Order",
                "count":1,
                "registry": True,
                "operation": "insert_document"
            }
           }, status_code = 201)