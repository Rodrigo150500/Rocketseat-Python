import pytest
from .pessoa_realizar_extrato_validator import pessoa_realizar_extrato_validator

class MockPerson():
    def __init__(self,body) -> None:
        self.body = body

def test_pessoa_realizar_extrato():
    
    http_request = MockPerson(body={
        "nome":"Rodrigo"
    })

    pessoa_realizar_extrato_validator(http_request)

def test_pessoa_realizar_extrato_error():
    
    http_request = MockPerson(body={
        "nome":15
    })

    with pytest.raises(Exception):
        pessoa_realizar_extrato_validator(http_request)