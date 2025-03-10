from .password_handler import PasswordHandler

def test_encrypt_password():

    password_handler = PasswordHandler()

    password = "abc123"

    hashed_password = password_handler.encrypt_password(password)

    check_password = password_handler.check_password(password, hashed_password)

    assert check_password == True