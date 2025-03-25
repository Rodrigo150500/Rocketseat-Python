from pydantic import BaseModel, ValidationError, constr
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntity


def pessoa_realizar_extrato_validator(http_request: HttpRequest):

    class BodyData(BaseModel):

        nome: constr(min_length = 1)

    try:

        BodyData(**http_request.body)

    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors())