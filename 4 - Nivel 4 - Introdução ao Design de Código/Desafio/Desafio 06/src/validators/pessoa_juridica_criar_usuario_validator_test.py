import pytest
from .pessoa_juridica_criar_usuario_validator import pessoa_juridica_criar_usuario_validator

class MockPerson:
    def __init__(self, body) -> None:
        self.body = body

def test_pessoa_juridica_criar_usuario():

    http_request = MockPerson(body={
        "faturamento": 156.98, 
        "idade": 22,
        "nome_fantasia": "Rodrigo Company",
        "celular": "(11) 5487-8966",
        "email_corporativo": "rodrigo@gmail.com",
        "categoria": "Categoria A",
        "saldo": 458.99
    })

    pessoa_juridica_criar_usuario_validator(http_request)

def test_pessoa_juridica_criar_usuario_error():

    http_request = MockPerson(body={
        "faturamento": "156.98", 
        "idade": 22,
        "nome_fantasia": "Rodrigo Company",
        "celular": "(11) 5487-8966",
        "email_corporativo": "rodrigo@gmail.com",
        "categoria": "Categoria A",
        "saldo": 458.99
    })

    with pytest.raises(Exception):
        pessoa_juridica_criar_usuario_validator(http_request)