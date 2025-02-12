import sqlite3
from sqlite3 import Connection

class __DbConnectionHandler:
    def __init__(self):
        self.__conection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        self.__conn = sqlite3.connect(self.__conection_string)

    def get_connection(self) -> Connection:
        return self.__conn

db_connection_handler = __DbConnectionHandler()