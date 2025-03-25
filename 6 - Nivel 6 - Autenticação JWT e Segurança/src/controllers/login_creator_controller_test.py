import pytest
from src.controllers.login_creator_controller import LoginCreatorController
from src.drivers.password_handler import PasswordHandler

username = "Rodrigo"
password = "123ABC"
hashed_password = PasswordHandler().encrypt_password(password)


class MockRepository:
    def get_user_by_username(self, username):
        return (10, username, hashed_password)

def test_login_creator():

    mock_repository = MockRepository()
    
    login_creator = LoginCreatorController(mock_repository)

    response = login_creator.creator(username, password)

    assert response['acess'] == True
    assert response['username'] == username
    assert response['token'] is not None

def test_login_with_error_password():

    mock_repository = MockRepository()

    login_creator = LoginCreatorController(mock_repository)

    with pytest.raises(Exception):
        login_creator(username, "senha")
