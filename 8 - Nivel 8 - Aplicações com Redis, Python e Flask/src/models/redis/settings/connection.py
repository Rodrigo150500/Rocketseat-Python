from redis import Redis

class RedisConnectionHandler:
    def __init__(self):
        self.__redis_conn = None
    
    def connect(self) -> Redis:
        redis_conn = Redis(host="localhost", port=6379, db=0)

        self.__redis_conn = redis_conn

        return redis_conn

    def get_connection(self) -> Redis:

        return self.__redis_conn