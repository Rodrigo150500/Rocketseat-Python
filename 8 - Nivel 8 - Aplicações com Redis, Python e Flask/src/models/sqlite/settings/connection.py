import sqlite3
from sqlite3 import Connection as SQLiteConnection

class SqliteConnectionHandler:

    def __init__(self):
        self.__connection_string = "storage.db"
        self.__conn = None
    
    def connect(self) -> SQLiteConnection:
        conn = sqlite3.connect(self.__connection_string, check_same_thread= False)

        self.__conn = conn
        return conn

    def get_connection(self) -> SQLiteConnection:
        return self.__conn