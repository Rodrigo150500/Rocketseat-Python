import pytest
from .pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Teste de Integração")
def test_realizar_extrato():
    nome = "João da Silva"
    
    repo = PessoaFisicaRepository(db_connection_handler)

    response = repo.realizar_extrato(nome)
    print()

    print(response)
    