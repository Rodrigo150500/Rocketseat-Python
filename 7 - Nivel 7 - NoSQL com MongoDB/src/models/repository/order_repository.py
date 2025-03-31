from pymongo.database import Database

class OrderRepository:
    
    def __init__(self, db_connection:Database):
        self.__collection_name = "orders"
        self.__db_connection = db_connection
        
    def insert_document(self, document: dict) -> None:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
    
    def insert_many_documents(self, documents: list) -> None:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(documents)