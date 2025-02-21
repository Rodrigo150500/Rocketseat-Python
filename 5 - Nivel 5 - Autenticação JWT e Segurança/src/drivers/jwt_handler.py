import jwt
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_configs

class JwtHandler:

    def create_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours= int(jwt_configs['JWT_HOURS'])),
                **body
            },
            key = jwt_configs['KEY'],
            algorithm= jwt_configs['ALGORITHM']
        )

        return token

    def decode_token(self, token: str) -> dict:

        token_information = jwt.decode(
                                token, 
                                key='minhaSenha', 
                                algorithms=['HS256'])

        return token_information

