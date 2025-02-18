from .user_repository import UserRepository
from unittest.mock import Mock


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_registry_user():

    mock_connection = MockConnection()

    repo = UserRepository(mock_connection)

    username = "Rodrigo"
    password = "Issao"

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert (username, password, 0) == cursor.execute.call_args[0][1]

def test_edit_balance():

    mock_connetion = MockConnection()

    repo = UserRepository(mock_connetion)

    userID = 122
    balance = 99.95

    repo.edit_balance(userID, balance)

    cursor = mock_connetion.cursor.return_value

    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert (balance, userID) == cursor.execute.call_args[0][1]

    mock_connetion.commit.assert_called_once()

def test_get_user_by_name():
    
    mock_connection = MockConnection()

    repo = UserRepository(mock_connection)

    username = "Rodrigo"
    repo.get_user_by_username(username)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password, balance" in cursor.execute.call_args[0][0] 
    assert "FROM users" in cursor.execute.call_args[0][0] 
    assert "WHERE username = ?" in cursor.execute.call_args[0][0] 

    cursor.fetchone.assert_called_once()