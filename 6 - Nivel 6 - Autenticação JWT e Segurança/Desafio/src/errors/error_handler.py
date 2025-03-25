from src.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequest
from .error_types.http_not_found import HttpNotFound
from .error_types.http_unauthorized import HttpUnauthorized
from .error_types.http_unprocessable_entity import HttpUnprocessableEntity

def error_handler(error: Exception):

    if isinstance(error, (HttpBadRequest, HttpNotFound, HttpUnauthorized, HttpUnprocessableEntity)):
                
        return HttpResponse(body={
            "title": error.name,
            "details": error.message
        }, status_code = error.status_code)
    else:
        return HttpResponse( body={
            "title": "Server error",
            "details": str(error)
        }, status_code= 500)