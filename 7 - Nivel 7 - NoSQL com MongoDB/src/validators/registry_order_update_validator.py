from cerberus import Validator
from src.errors.types.http_unprocessable_entity_error import HttpUnprocessableEntity

def registry_order_update_validator(body: any):

    body_validator = Validator(
        {
            "data":{
                "type": "dict",
                "schema":{
                    "name": {"type": "string"},
                    "address": {"type": "string"},
                    "cupom": {"type": "boolean"}
                }
            }
        }
    )

    response = body_validator.validate(body)

    if response is False:
        raise HttpUnprocessableEntity(body_validator.errors)

    