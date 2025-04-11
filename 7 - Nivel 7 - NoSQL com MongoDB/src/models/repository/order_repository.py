from bson import ObjectId

class OrderRepository:
    
    def __init__(self, db_connection):
        self.__collection_name = "orders"
        self.__db_connection = db_connection
        
    def insert_document(self, document: dict) -> None:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
    
    def insert_many_documents(self, documents: list) -> None:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(doc_filter)

        return response
    
    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
            
        return response

    def select_with_many_properties(self, doc_filter: dict) -> list:

        collection = self.__db_connection.get_collection(self.__collection_name)

        response = collection.find(
            doc_filter,
            {"_id":0, "cupom": 0}
        )

        return response                         

    def select_if_exists(self) -> list:

        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find({
            "address":{
                "$exists": True
            }},
            {"_id":0}
            
        )

        return response

    def select_by_object_id(self, object_id: str) -> dict:

        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({
            "_id": ObjectId(object_id)
        })


        return response

    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId("67e9e8db472d9f9cecc59588")}, #filtro
            {"$set":{"itens.refrigerante.quantidade": 999}}  #Edição
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            {"tipo.refrigerante.quantidade": {"$exists": True}}, #filtro
            {"$set":{"itens.refrigerante.quantidade": 999}}  #Edição
        )

    def edit_registry_with_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)

        collection.update_one(
            {"_id":ObjectId("67e9e8db472d9f9cecc59588")},
            {"$inc":{"tipo.refrigerante.quantidade": 55}}
        )

    def delete_registry(self) -> None:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one(
            {"_id": ObjectId('67e9e8db472d9f9cecc59588')}
        )

    def delete_many_registries(self) -> None:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(
            {"cupom": True}
        )
