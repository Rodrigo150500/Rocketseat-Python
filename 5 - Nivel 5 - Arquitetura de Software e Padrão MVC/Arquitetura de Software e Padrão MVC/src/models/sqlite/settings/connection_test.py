import pytest
from sqlalchemy.engine import Engine
from .connection import db_connect_handler

@pytest.mark.skip(reason="Interação com o BD")
def test_connect_to_db():
    
    assert db_connect_handler.get_engine() is None

    db_connect_handler.conect_to_db()

    db_engine = db_connect_handler.get_engine()

    assert db_engine is not None

    assert isinstance(db_engine, Engine)
    
    