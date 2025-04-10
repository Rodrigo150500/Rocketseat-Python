from .order_repository import OrderRepository
from typing import Any

class MockCollection:

    def __init__(self) -> None:
        self.insert_one_attributes = {}
        self.find_attributes = {}

    def insert_one(self, document: Any) -> None:
        self.insert_one_attributes["dict"] = document

    def find(self, *args):
        self.find_attributes["args"] = args

class DBMockConnection:

    def __init__(self, collection) -> None:
        self.get_collection_attributes = {}
        self.collection = collection
    
    def get_collection(self, collection_name):
        self.get_collection_attributes["name"] = collection_name
        return self.collection

def test_insert_document():

    collection  = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection) #type: ignore

    doc = {"alguma": "coisa"}

    repo.insert_document(doc)

    print()

    assert collection.insert_one_attributes['dict'] == doc

def test_select_with_many_properties():

    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection) #type: ignore

    doc = {"testando": "algo"}

    repo.select_with_many_properties(doc)

    assert collection.find_attributes["args"][0] == doc
    assert collection.find_attributes["args"][1] == {"_id":0, "cupom": 0}

    


