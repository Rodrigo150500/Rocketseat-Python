import os

jwt_configs = {
    "KEY": os.getenv("KEY"),
    "ALGORITHM": os.getenv("ALGORITHM"),
    "JWT_HOURS": os.getenv("JWT_HOURS")
}