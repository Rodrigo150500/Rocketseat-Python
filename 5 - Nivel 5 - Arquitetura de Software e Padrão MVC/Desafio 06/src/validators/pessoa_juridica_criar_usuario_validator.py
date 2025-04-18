from pydantic import BaseModel, constr, ValidationError, StrictInt, StrictFloat
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntity
from src.views.http_types.http_request import HttpRequest

def pessoa_juridica_criar_usuario_validator(http_request: HttpRequest):

    class BodyData(BaseModel):
        faturamento: StrictFloat
        idade: StrictInt
        nome_fantasia: constr(min_length=1)
        celular: constr(min_length=1)
        email_corporativo: constr(min_length=1)
        categoria: constr(min_length=1)
        saldo: StrictFloat

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors())