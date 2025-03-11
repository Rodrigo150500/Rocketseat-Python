from .jwt_handler import JwtHandler

def test_encode_jwt():

    jwt_handler = JwtHandler()

    body = {
        "user_id": 10
    }

    token = jwt_handler.create_token(body)

    token_info = jwt_handler.decode_token(token)

    assert isinstance(token_info, dict)
    assert token_info["user_id"] == 10