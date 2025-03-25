from .conection import db_conection_handler
from sqlite3 import Connection

def test_conection():


    assert db_conection_handler.get_connection() is None
    
    db_conection_handler.connect()

    db_engine = db_conection_handler.get_connection()

    assert isinstance(db_engine, Connection)
    
    assert db_conection_handler is not None

