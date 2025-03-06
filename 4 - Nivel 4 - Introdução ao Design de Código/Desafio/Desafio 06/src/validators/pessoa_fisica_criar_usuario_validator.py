from pydantic import BaseModel, constr, ValidationError
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntity
from src.views.http_types.http_request import HttpRequest

def pessoa_fisica_criar_usuario_validator(http_request: HttpRequest):

    class BodyData(BaseModel):
        nome_completo: constr(min_length=1)
        idade : int
        categoria : constr(min_length=1)
        celular : constr(min_length=1)
        email : constr(min_length=1)
        saldo : float
        renda_mensal : float

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors())