import sqlite3
from sqlite3 import Connection

class __ConectionHandler:
    def __init__(self) -> None:
        self.__conection_string = "desafio07.db"
        self.__conn = None
    
    def connect(self) -> None:
        self.__conn = sqlite3.connect(
                        self.__conection_string, 
                        check_same_thread=False)

    def get_connection(self) -> Connection:
        return self.__conn

db_conection_handler = __ConectionHandler()