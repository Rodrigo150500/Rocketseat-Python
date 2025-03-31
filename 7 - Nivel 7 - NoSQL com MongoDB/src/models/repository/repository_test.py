import pytest
from src.models.connections.connection_handler import DBConnectionHanler
from .order_repository import OrderRepository


db_connection_handler = DBConnectionHanler()
db_connection_handler.connection_to_db()
conn = db_connection_handler.get_db_connection()

if conn is None:
    raise Exception("Database out of connection")

@pytest.mark.skip(reason="Teste de Integração")
def test_insert_document():


    order_repository = OrderRepository(conn)

    my_doc = {"chave":{
        "Ola": "Mundo",
        'Amanhã':"Luta"
    }
    }
    order_repository.insert_document(my_doc)

@pytest.mark.skip(reason="Teste de Integração")
def test_insert_many_documents():

    order_repository = OrderRepository(conn)

    my_doc = [
        {
            "nome":"Rogerio",
            "Data Nascimento": "15/09/24",
            "Comida Favorita": ["Arroz, feijão"]
        },
        {
            "nome":"Adalbeti",
            "Data Nascimento": "05/02/1968",
            "Comida Favorita": ["Prato"]
        }
    ]

    order_repository.insert_many_documents(my_doc)

