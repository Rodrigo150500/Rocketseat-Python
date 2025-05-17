from src.models.redis.interface.redis_repository import RedisRepositoryInterface
from src.models.sqlite.interface.products_repository import ProductsRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductCreator:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductsRepositoryInterface):
        self.__repo_redis = redis_repo
        self.__products_repo = products_repo
    
    def create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        name = body.get("name")
        price = body.get("price")
        quantity = body.get("quantity")
    
    def __insert_in_sqlite(self, name: str, price: float, quantity: int) ->None:
        self.__products_repo.insert_product(name, price, quantity)
    
    def __insert_in_cache(self, name: str, price: float, quantity: int) -> None:

        product_key = name

        value = f'{price}, {quantity}'

        self.__repo_redis.insert_ex(product_key, value, ex=60)
    
    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            status_code=201,
            body={
                "type": "PRODUCT",
                "count":1,
                "message": "Product created succesfully"
            }
        )