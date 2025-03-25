from .jwt_handler import JwtHandler

def test_jwt_handler():

    jwt_handler = JwtHandler()

    body = {
        "username": "Rodrigo",
        "email": "rodrigo.takara@gmail.com"
    }

    token = jwt_handler.create_token(body)
    token_info = jwt_handler.decode_token(token)

    assert token is not None
    assert token_info['username'] == "Rodrigo"
    assert token_info['email'] == "rodrigo.takara@gmail.com"
