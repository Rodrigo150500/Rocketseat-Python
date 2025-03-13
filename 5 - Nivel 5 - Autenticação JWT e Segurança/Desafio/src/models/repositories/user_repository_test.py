from datetime import datetime

from .user_repository import UserRepository
from unittest.mock import Mock


class MockCursor:
    def __init__(self) -> None:
        self.fetchone = Mock()
        self.fetchall = Mock()
        self.execute = Mock()


class MockConection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_registry_user():
    
    conn = MockConection()

    repo = UserRepository(conn)

    repo.registry_user("Rodrigo", "123ABC")

    cursor = conn.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert ("Rodrigo", "123ABC") == cursor.execute.call_args[0][1]
    

def test_get_user_by_username():

    conn = MockConection()

    repo = UserRepository(conn)

    repo.get_user_by_username("Rodrigo")

    cursor = conn.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert ("Rodrigo",) == cursor.execute.call_args[0][1]

def test_list_all_tasks_by_user_id():

    conn = MockConection()

    repo = UserRepository(conn)

    repo.list_all_tasks_by_user_id(1)

    cursor = conn.cursor.return_value

    assert "SELECT id, date_order, task_name, task_detail" in cursor.execute.call_args[0][0]
    assert "FROM orders" in cursor.execute.call_args[0][0]
    assert "WHERE user_id == ?" in cursor.execute.call_args[0][0]
    assert (1,) == cursor.execute.call_args[0][1]

def test_create_new_task():

    conn = MockConection()

    repo = UserRepository(conn)

    repo.create_new_task(1,"Fazer limpeza", "Limpar cozinha e quartos")

    cursor = conn.cursor.return_value

    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    assert "INSERT INTO orders" in cursor.execute.call_args[0][0]
    assert "(user_id, date_order, task_name, task_detail)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert "(?, ?, ?, ?)" in cursor.execute.call_args[0][0]
    assert (1, date,"Fazer limpeza", "Limpar cozinha e quartos") == cursor.execute.call_args[0][1]

