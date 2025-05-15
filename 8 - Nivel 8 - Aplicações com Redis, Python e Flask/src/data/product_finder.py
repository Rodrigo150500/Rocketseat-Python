from src.models.redis.interface.redis_repository import RedisRepositoryInterface
from src.models.sqlite.interface.products_repository import ProductsRepositoryInterface

class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductsRepositoryInterface):
        self.__repo_redis = redis_repo
        self.__products_repo = products_repo
        