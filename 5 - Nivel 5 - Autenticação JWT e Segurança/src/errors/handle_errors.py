from src.views.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequest
from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unauthorized import HttpUnauthorized

def handle_errors(error: Exception) -> HttpResponse:

    if isinstance(error, (HttpBadRequest, HttpNotFound, HttpUnauthorized)):
        return HttpResponse(
            body={
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]
            },
            status_code=error.status_code
        )
    
    return HttpResponse(
        body={
            "error":{
                "title": "Server Error",
                "detail": str(error)
            }
        },
        status_code= 500
    )

