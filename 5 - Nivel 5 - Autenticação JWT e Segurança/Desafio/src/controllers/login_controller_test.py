from .login_controller import LoginController
from src.drivers.password_handler import PasswordHandler

class MockRepository:

    def encrypt_password(self):
        
        password = "ABC123"
        
        hashed_password = PasswordHandler().encrypt_password(password)
       
        return hashed_password

    def get_user_by_username(self, username):

        hashed_password = self.encrypt_password()
        
        return (1, 'Rodrigo', hashed_password)

def test_login():

    repo = MockRepository()

    controller = LoginController(repo)

    response = controller.login("Rodrigo", "ABC123")

    assert response["data"]["access"] == True
    assert response["data"]["username"] == "Rodrigo"
    assert response["data"]["token"] is not None

    