import pytest
from .user_repository import UserRepository
from src.models.settings.conection import db_conection_handler



@pytest.mark.skip(reason="Teste de Integração")
def test_registry_user_integration():

    db_conection_handler.connect()

    conn = db_conection_handler.get_connection()

    repo = UserRepository(conn)

    username = "Rodrigo"
    password = "ABC123"

    repo.registry_user(username, password)

@pytest.mark.skip(reason="Teste de Integração")
def test_get_user_by_username():

    db_conection_handler.connect()

    conn = db_conection_handler.get_connection()

    repo = UserRepository(conn)

    user = repo.get_user_by_username("Rodrigo")

    assert isinstance(user, tuple)
    assert user[0] == 1
    assert user[1] == "Rodrigo"
    assert user[2] == "ABC123"

@pytest.mark.skip(reason="Teste de Integração")
def test_create_new_task():

    db_conection_handler.connect()

    conn = db_conection_handler.get_connection()
    
    repo = UserRepository(conn)

    user_id = 1
    task_name = "Limpeza Geral"
    task_detail = "Limpar quartos e salas"

    repo.create_new_task(user_id, task_name, task_detail)

@pytest.mark.skip(reason="Teste de Integração")
def test_list_all_tasks_by_user_id():

    db_conection_handler.connect()

    conn = db_conection_handler.get_connection()

    repo = UserRepository(conn)

    response = repo.list_all_tasks_by_user_id(1)

    print(response)
