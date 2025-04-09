#pylint: disable-all

import pytest
from src.models.connections.connection_handler import DBConnectionHanler
from .order_repository import OrderRepository


#db_connection_handler = DBConnectionHanler()
#db_connection_handler.connection_to_db()
#conn = db_connection_handler.get_db_connection()

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
@pytest.mark.skip(reason="Teste de Integração")
def test_select_many():

    order_repository = OrderRepository(conn)

    doc_filter = {
        "cupom": True
    }

    response = order_repository.select_many(doc_filter)

    print()
    print(response)

@pytest.mark.skip(reason="Teste de Integração")
def test_select_one():

    order_repository = OrderRepository(conn)

    doc_filter = {
        "cupom": True
    }

    response = order_repository.select_one(doc_filter)

    print()
    print(response)

@pytest.mark.skip("Teste de Integração")
def test_select_with_many_properties():

    order_repository = OrderRepository(conn)

    doc_filter = {
        "cupom": True
    }

    response = order_repository.select_with_many_properties(doc_filter)

    print(response)

@pytest.mark.skip("Teste de Integração")
def test_select_if_exists():

    order_repository = OrderRepository(conn)

    response = order_repository.select_if_exists()

    print(response)

@pytest.mark.skip("Teste de Integração")
def test_select_many_with_multiple_filter():

    order_repository = OrderRepository(conn)

    doc_filter = {
        "cupom": True,
        "itens.refrigerante": {"$exists": True}
    } #Semelhante a uma busca AND em SQL

    response = order_repository.select_many(doc_filter)

    print(response)

@pytest.mark.skip("Teste de Integração")
def test_select_many_with_or_filter():

    order_repository = OrderRepository(conn)

    doc_filter = {
        "$or":[
            {"address": {"$exists": True}},
            {"itens.pipoca":{"$exists": True}
            }]
    } #Semelhante a uma busca OR em SQL

    response = order_repository.select_many(doc_filter)

    print(response)

@pytest.mark.skip("Teste de Integração")
def test_select_by_object_id():

    order_repository = OrderRepository(conn)

    response = order_repository.select_by_object_id("67ed0783df6150f8f67dbe8f")

    print(response)
@pytest.mark.skip("Teste de Integração")
def test_edit_selection():

    order_repository = OrderRepository(conn)

    order_repository.edit_registry()

@pytest.mark.skip("Teste de Integração")
def test_edit_many_registries():

    order_repostory = OrderRepository(conn)

    order_repostory.edit_many_registries()

@pytest.mark.skip("Teste de Integração")
def test_edit_registry_with_increment():

    order_repostory = OrderRepository(conn)

    order_repostory.edit_registry_with_increment()

@pytest.mark.skip("Teste de Integração")
def test_delete_registry():

    order_repository = OrderRepository(conn)
    order_repository.delete_registry()

@pytest.mark.skip("Teste de Integração")
def test_delete_many_registries():

    order_repository = OrderRepository(conn)
    order_repository.delete_many_registries()
    
