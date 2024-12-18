from typing import Dict
from src.errors.http_bad_request import HttpBadRequestError 
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

def handler_error(error: Exception) -> Dict:
    if isinstance(error, (HttpBadRequestError, HttpUnprocessableEntityError)):
        return {
            "status_code": error.status_code,
            "body":{
                "errors":[{
                    "title": error.name,
                    "details": error.message
                }]
            }
        }
    
    return {
        "status_code": 500,
        "body":{
            "errors":[{
                "title": "Server Error",
                "details": str(error)
            }]
        }
    }