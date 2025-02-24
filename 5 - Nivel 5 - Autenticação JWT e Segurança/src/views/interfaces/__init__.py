from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class ViewInterface(ABC):

    def handle(self, http_reques: HttpRequest) -> HttpResponse:
        pass