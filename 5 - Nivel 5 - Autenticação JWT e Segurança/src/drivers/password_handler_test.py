from .password_handler import PasswordHandler

def test_password_handler():

    password_handler = PasswordHandler()

    minha_senha = "123ABC"

    hashed_password = password_handler.encrypt_password(minha_senha)

    check_password = password_handler.check_password(minha_senha, hashed_password)

    assert check_password