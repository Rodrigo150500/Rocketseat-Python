import pytest
from .pessoa_fisica_criar_usuario_validator import pessoa_fisica_criar_usuario_validator

class MockPerson:
    def __init__(self,body) -> None:
        self.body = body


def test_pessoa_criar_usuario():

    mock_request = MockPerson(body={
        "nome_completo": "Rodrigo",
        "idade" : 15,
        "categoria" : "Categoria S",
        "celular" : "(11) 6658-6588",
        "email" : "Rodrigo.gmail.com",
        "saldo" : 165.99,
        "renda_mensal" : 1548.66
    })

    pessoa_fisica_criar_usuario_validator(mock_request)

def test_pessoa_fisica_criar_usuario_error():

    mock_request = MockPerson(body={
        "nome_completo": 1564,
        "idade" : "15",
        "categoria" : "Categoria S",
        "celular" : "(11) 6658-6588",
        "email" : "Rodrigo.gmail.com",
        "saldo" : 165.99,
        "renda_mensal" : 1548.66
    })

    with pytest.raises(Exception):
        pessoa_fisica_criar_usuario_validator(mock_request)