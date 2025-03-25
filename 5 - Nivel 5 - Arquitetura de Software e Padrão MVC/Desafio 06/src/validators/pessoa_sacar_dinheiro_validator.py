from pydantic import BaseModel, ValidationError, constr, StrictFloat
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntity

def pessoa_sacar_dinheiro_validator(http_request: HttpRequest):

    class BodyData(BaseModel):

        nome: constr(min_length=1)
        saque: StrictFloat
    
    try:
        BodyData(**http_request.body)
    
    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors())