import pytest
from .pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

class PessoaFisica:

    def __init__(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.renda_mensal = renda_mensal
        self.idade = idade
        self.nome_completo = nome_completo
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo


@pytest.mark.skip(reason="Teste de Integração")
def test_realizar_extrato():
    nome = "João da Silva"
    
    repo = PessoaFisicaRepository(db_connection_handler)

    response = repo.realizar_extrato(nome)
    
    print()

    print(response)

@pytest.mark.skip(reason="Teste de Integração")
def test_criar_usuario():

    usuario = PessoaFisica(1920,15,"Jorge Silva Campo", "(55) 95154-8942", "Jorge.Silva@gmail.com", "Categoria A", 1500)

    repo = PessoaFisicaRepository(db_connection_handler)

    repo.criar_usuario(usuario)

    


    
    