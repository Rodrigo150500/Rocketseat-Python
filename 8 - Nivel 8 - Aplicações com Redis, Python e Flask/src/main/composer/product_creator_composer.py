from src.main.server.server_settings import redis_connection_handle, sqlite_connection_handle

from src.models.redis.repositories.redis_repository import RedisRepository
from src.models.sqlite.repository.products_repository import ProductsRepository

from src.data.product_creator import ProductCreator


def product_creator_composer():
    
    redis_conn = redis_connection_handle.get_connection()
    sqlite_conn = sqlite_connection_handle.get_connection()

    redis_repo = RedisRepository(redis_conn)
    products_repo = ProductsRepository(sqlite_conn)

    return ProductCreator(redis_repo, products_repo)