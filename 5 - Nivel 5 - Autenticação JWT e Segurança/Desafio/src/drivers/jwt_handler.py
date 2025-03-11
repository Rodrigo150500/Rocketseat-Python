import jwt
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_config

class JwtHandler:

    def create_token(self, body: dict = {}) -> str:
        encode_jwt = jwt.encode(payload={
            'exp':datetime.now(timezone.utc)+ timedelta(hours=int(jwt_config["JWT_HOURS"])),
            **body
        },
        key=jwt_config["KEY"],
        algorithm=jwt_config['ALGORITHM']
        )

        return encode_jwt

    def decode_token(self, token: str) -> dict:

        token_info = jwt.decode(token, key=jwt_config["KEY"], algorithms=jwt_config['ALGORITHM'])

        return token_info