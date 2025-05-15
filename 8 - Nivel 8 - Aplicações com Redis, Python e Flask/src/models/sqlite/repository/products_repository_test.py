import pytest
from .products_repository import ProductsRepository
from src.models.sqlite.settings.connection import SqliteConnectionHandler

conn_handle = SqliteConnectionHandler()
conn = conn_handle.connect()

@pytest.mark.skip(reason="Integração com banco de dados")
def test_insert_product():
    repo = ProductsRepository(conn)

    name = "meu"
    price = 12.85
    quantity = 2

    repo.insert_product(name, price, quantity)

@pytest.mark.skip(reason="Integração com banco de dados")
def test_get_product_by_name():
    repo = ProductsRepository(conn)

    name = "meu"

    response = repo.find_product_by_name(name)
    print(response)
