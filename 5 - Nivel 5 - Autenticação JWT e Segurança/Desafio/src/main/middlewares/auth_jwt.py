from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.errors.error_types.http_unauthorized import HttpUnauthorized

def auth_jwt():

    jwt_handler = JwtHandler()

    token_raw = request.headers["authorization"]
    user_uid = request.headers["uid"]

    if token_raw != user_uid:
        HttpUnauthorized("Invalid Auth Unauthorized")
    
    token = token_raw.split()[1]
    payload = jwt_handler.decode_token(token)
    payload_user_id = payload["user_id"]

    if(payload_user_id) != user_uid:
        raise HttpUnauthorized("User unauthorized")
    
    return payload