from pymongo import MongoClient


class DBConnectionHanler:

    def __init__(self):

        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            "admin",
            "password",
            "localhost",
            "27017"
        )
        self.__database_name = "rocket_db"
        self.__client = None
        self.__db_connection = None

    def connection_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
    
    def get_db_connection(self):
        return self.__db_connection