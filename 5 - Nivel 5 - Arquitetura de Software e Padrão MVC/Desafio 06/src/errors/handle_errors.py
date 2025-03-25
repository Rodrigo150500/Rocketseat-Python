from flask import jsonify

from src.errors.errors_types.http_bad_request import HttpBadRequest
from src.errors.errors_types.http_not_found import HttpNotFound
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntity

from src.views.http_types.http_response import HttpResponse

def handle_errors(error: Exception):

    if isinstance(error, (HttpBadRequest, HttpNotFound, HttpUnprocessableEntity)):
        return HttpResponse(
            body=[{
                "title": error.name,
                "detail": error.message
            }], 
            status_code = error.status_code
        )
    
    return HttpResponse(
        body = [{
            "title": "Server Error",
            "detail": str(error)
        }],
        status_code= 500
    )