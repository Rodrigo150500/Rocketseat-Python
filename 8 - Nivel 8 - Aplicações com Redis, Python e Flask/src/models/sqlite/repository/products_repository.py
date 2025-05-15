from sqlite3 import Connection as SqliteConnection
from src.models.sqlite.interface.products_repository import ProductsRepositoryInterface

class ProductsRepository(ProductsRepositoryInterface):
    def __init__(self, conn: SqliteConnection) -> None:
        self.__conn = conn

    def find_product_by_name(self, product_name: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?",
            (product_name,)
        )
        product = cursor.fetchone()
        return product

    def insert_product(self, name: str, price: float, quantity: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO products
                    (name, price, quantity)
                VALUES
                (?, ?, ?)
            ''',
            (name, price, quantity,)
        )
        self.__conn.commit()