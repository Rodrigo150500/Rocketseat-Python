from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.errors.types.http_unauthorized import HttpUnauthorized

def auth_jwt_verify():

    jwt_handler = JwtHandler()

    token_raw = request.headers.get("Authorization")
    header_uid = request.headers.get('uid')

    if not token_raw or not header_uid:
        raise HttpUnauthorized("Invalid Auth Information")
    
    token = token_raw.split()[1]
    token_information = jwt_handler.decode_token(token)
    token_uid = token_information['user_id']

    if header_uid and token_uid and (int(token_uid) == int(header_uid)):
        return token_information
    
    raise HttpUnauthorized("User Unauthorized")

    

