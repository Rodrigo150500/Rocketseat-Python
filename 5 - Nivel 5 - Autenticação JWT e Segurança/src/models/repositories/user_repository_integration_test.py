import pytest
from .user_repository import UserRepository
from src.models.settings.db_connecting_handler import db_connection_handler

@pytest.mark.skip(reason="Teste de Integração")
def test_registry_user():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()

    repo = UserRepository(conn)

    username = "Rodrigo"
    password = "Takara"

    repo.registry_user(username, password)


@pytest.mark.skip(reason="Integração com banco de dados")
def test_edit_balance():

    db_connection_handler.connect()

    conn = db_connection_handler.get_connection()

    repo = UserRepository(conn)

    id_user = 1
    balance = 5.95
    repo.edit_balance(id_user, balance)

@pytest.mark.skip(reason="Integração com banco de dados")
def test_get_user_by_username():

    db_connection_handler.connect()

    conn = db_connection_handler.get_connection()

    repo = UserRepository(conn)

    username = "Rodrigo"

    user = repo.get_user_by_username(username)

    print()
    print(user)