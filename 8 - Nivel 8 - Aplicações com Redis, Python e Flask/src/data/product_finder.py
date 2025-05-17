from src.models.redis.interface.redis_repository import RedisRepositoryInterface
from src.models.sqlite.interface.products_repository import ProductsRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductsRepositoryInterface):
        self.__repo_redis = redis_repo
        self.__products_repo = products_repo
    
    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        
        product_name = http_request.params["product_name"]

        product = None

        product = self.__search_in_cache(product_name)

        if not product:
            product = self.__search_in_sqlite(product_name)
            self.__insert_in_cache(product)

        return HttpResponse(product)




    def __search_in_cache(self, product_name: str) -> tuple:

        product_info = self.__repo_redis.get_key(product_name).decode("utf-8") 

        if product_info:
            product_info_list = product_info.split(",") #value,quantity
            value = product_info_list[1]
            quantity = product_info_list[2]
            return (0, product_name, value, quantity)
        
        return None

    def __search_in_sqlite(self, product_name: str) -> tuple:
        product_info = self.__products_repo.find_product_by_name(product_name)

        if not product_info:
            raise Exception("Product not found")
        
        return product_info
    
    def __insert_in_cache(self, product: tuple) -> None:
        key = product[1]
        value = f'{product[2],{product[3]}}' 
        self.__repo_redis.insert_ex(key, value, ex=60)

    def __format_response(self, product: tuple) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "type": "PRODUCT",
                "count": 1,
                "attributes": {
                    "name": product[1],
                    "price": product[2],
                    "quantity": product[3]
                }
            }
        )