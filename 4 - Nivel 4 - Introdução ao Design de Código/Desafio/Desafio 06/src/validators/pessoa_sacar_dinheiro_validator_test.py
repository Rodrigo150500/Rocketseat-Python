import pytest
from .pessoa_sacar_dinheiro_validator import pessoa_sacar_dinheiro_validator

class MockPerson:

    def __init__(self, body) -> None:
        self.body = body

def test_pessoa_sacar_dinheiro_validator():

    http_request = MockPerson(body={
        "nome": "Rodrigo",
        "saque": 15.99
    })

    pessoa_sacar_dinheiro_validator(http_request)

def test_pessoa_sacar_dinheiro_validator_error():

    http_request = MockPerson(body={
        "nome": 2516,
        "saque": "15.99"
    })

    with pytest.raises(Exception):
        pessoa_sacar_dinheiro_validator(http_request)