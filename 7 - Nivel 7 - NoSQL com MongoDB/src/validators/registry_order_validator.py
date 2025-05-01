from cerberus import Validator
from src.errors.types.http_unprocessable_entity_error import HttpUnprocessableEntity

def registry_order_validator(body: any):

    body_validator = Validator({
        "data":{
            "type":"dict",
            "schema":{
                "name": {"type": "string", "required": True},
                "address": {"type": "string", "required": True},
                "cupom": {"type": "boolean", "required": True},
                "items":{
                    "type": "list",
                    "schema":{
                        "type": "dict",
                        "schema":{
                            "item":{"type": "string", "required": True},
                            "quantidade": {"type": "integer", "required": True}
                        }
                    }
                }
            }
        }
    })

    response = body_validator.validate(body)

    if response is False:
        raise HttpUnprocessableEntity(body_validator.errors)