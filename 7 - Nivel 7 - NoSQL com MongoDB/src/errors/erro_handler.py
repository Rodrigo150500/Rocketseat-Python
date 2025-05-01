from .types.http_not_found_error import HttpNotFoundError
from .types.http_unprocessable_entity_error import HttpUnprocessableEntity
from src.main.http_types.http_response import HttpResponse


def error_handler(error: Exception):

    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntity)):

        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors":[{
                "title": "Error Server",
                "detail": str(error)
            }]
        }
    )