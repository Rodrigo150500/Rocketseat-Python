from bson import ObjectId
from .order_repository import OrderRepository
from typing import Any

class MockCollection:

    def __init__(self) -> None:
        self.insert_one_attributes = {}
        self.find_attributes = {}
        self.insert_many_attributes = {}
        self.find_one_attributes = {}
        self.update_one_attributes = {}
        self.update_many_attributes = {}
        self.delete_one_attributes = {}
        self.delete_many_attributes = {}

    def insert_one(self, document: Any) -> None:
        self.insert_one_attributes["dict"] = document
    
    def insert_many(self, documents: Any) -> None:
        self.insert_many_attributes["dict"] = documents
    
    def find(self, *args):
        self.find_attributes["args"] = args    
    
    def find_one(self, *args):
        self.find_one_attributes["args"] = args

    def update_one(self, *args):
        self.update_one_attributes["args"] = args

    def update_many(self, *args):
        self.update_many_attributes["args"] = args

    def delete_one(self, *args):
        self.delete_one_attributes["args"] = args
    
    def delete_many(self, *args):
        self.delete_many_attributes["args"] = args

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

def test_insert_many_documents():

    collection = MockCollection()

    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection)

    doc = [
        {"alguma": "coisa"},
        {"algumas": "coisas"}
    ]

    repo.insert_many_documents(doc)


    assert collection.insert_many_attributes["dict"] == doc


def test_select_if_exists():

    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)
    repo = OrderRepository(db_mock_connection)

    repo.select_if_exists()

    assert collection.find_attributes["args"][0] == {"address":{"$exists": True}}
    assert collection.find_attributes["args"][1] == {"_id":0}

def test_select_one():

    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection)

    doc = {"filtro": True}

    repo.select_one(doc)
    assert collection.find_one_attributes["args"][0] == doc            

def test_select_by_object_id():

    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection)

    user_id = "67f87cff912f29e0b480b9b7"

    repo.select_by_object_id(user_id)

    assert collection.find_one_attributes["args"][0] == {"_id": ObjectId(user_id)} 

def test_edit_registry():

    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection)

    repo.edit_registry()

    assert collection.update_one_attributes["args"][0] == {"_id": ObjectId("67e9e8db472d9f9cecc59588")}
    assert collection.update_one_attributes["args"][1] == {"$set":{"itens.refrigerante.quantidade": 999}}  

def test_edit_many_resgistries():
    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection)

    repo.edit_many_registries()

    assert collection.update_many_attributes["args"][0] == {"tipo.refrigerante.quantidade": {"$exists": True}}
    assert collection.update_many_attributes["args"][1] == {"$set":{"itens.refrigerante.quantidade": 999}}

def test_edit_registry_with_increment():
    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection)

    repo.edit_registry_with_increment()

    assert collection.update_one_attributes["args"][0] == {"_id":ObjectId("67e9e8db472d9f9cecc59588")}
    assert collection.update_one_attributes["args"][1] == {"$inc":{"tipo.refrigerante.quantidade": 55}}

def test_delete_registry():
    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection)

    repo.delete_registry()

    assert collection.delete_one_attributes["args"][0] == {"_id": ObjectId('67e9e8db472d9f9cecc59588')}

def test_delete_many_registry():
    collection = MockCollection()
    db_mock_connection = DBMockConnection(collection)

    repo = OrderRepository(db_mock_connection)

    repo.delete_many_registries()

    assert collection.delete_many_attributes["args"][0] == {"cupom": True}

