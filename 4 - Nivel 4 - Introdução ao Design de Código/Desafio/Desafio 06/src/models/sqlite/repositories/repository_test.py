import pytest
from .pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.settings.connection import db_connection_handler

from src.models.sqlite.repositories.pessoa_juridica import PessoaJuridicaRepository

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
def test_realizar_extrato_fisico():
    nome = "João da Silva"
    
    repo = PessoaFisicaRepository(db_connection_handler)

    response = repo.realizar_extrato(nome)
    
    print()

    print(response)

@pytest.mark.skip(reason="Teste de Integração")
def test_criar_usuario_fisico():

    usuario = PessoaFisica(1920,15,"Jorge Silva Campo", "(55) 95154-8942", "Jorge.Silva@gmail.com", "Categoria A", 1500)

    repo = PessoaFisicaRepository(db_connection_handler)

    repo.criar_usuario(usuario)

@pytest.mark.skip(reason="Teste de Integração")
def test_listar_usuarios_fisico():

    repo = PessoaFisicaRepository(db_connection_handler)

    response = repo.listar_usuarios()

    print()
    print(response)


    
@pytest.mark.skip(reason="Teste de Integração")
def test_sacar_dinheiro_fisico():

    repo = PessoaFisicaRepository(db_connection_handler)

    saldo = repo.sacar_dinheiro("Rodrigo", 5)

    print()
    print(saldo)

@pytest.mark.skip(reason="Teste de Integração")
def test_consultar_saldo_fisico():

    repo = PessoaFisicaRepository(db_connection_handler)

    saldo = repo.consultar_saldo("Rodrigo")

    print()

    print(saldo)

@pytest.mark.skip(reason="Teste de Integração")
def test_consultar_saldo_juridico():

    repo = PessoaJuridicaRepository(db_connection_handler)

    empresa = "Empresa XYZ"

    response = repo.consultar_saldo(empresa)

    assert isinstance(response, float)

    assert response == 50000

@pytest.mark.skip(reason="Teste de Integração")
def test_sacar_dinheiro_juridico():

    repo = PessoaJuridicaRepository(db_connection_handler)

    empresa = "Empresa XYZ"

    saque = 10000

    response = repo.sacar_dinheiro(empresa, saque)

    print(response)