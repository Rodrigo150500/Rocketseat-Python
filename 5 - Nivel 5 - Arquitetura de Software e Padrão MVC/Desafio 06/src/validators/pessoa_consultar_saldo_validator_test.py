import pytest
from .pessoa_consultar_saldo_validator import pessoa_consultar_saldo_validator


class MockRequest():

    def __init__(self, body) -> None:
        self.body = body

def test_consultar_saldo_validator():

    mock_request = MockRequest(body={
        "nome":"Rodrigo"
    })

    pessoa_consultar_saldo_validator(mock_request)

def test_consultar_saldo_validator_error():

    mock_request = MockRequest(body={
        "nome":154
    })

    with pytest.raises(Exception):
        pessoa_consultar_saldo_validator(mock_request)