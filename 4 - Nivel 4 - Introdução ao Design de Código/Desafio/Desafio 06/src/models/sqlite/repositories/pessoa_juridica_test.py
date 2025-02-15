from .pessoa_juridica import PessoaJuridicaRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.sqlite.interface.pessoa_juridica_atributos_interface import PessoaJuridicaAtributosInterface

class MockConnection:

    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(PessoaJuridicaTable)],
                    [PessoaJuridicaTable(
                        faturamento = 15900,
                        idade = 15,
                        nome_fantasia = "Roberto Company",
                        celular = "(55) 11 98756-6235",
                        email_corporativo = "Roberto.company@company.com",
                        categoria = "Categoria B",
                        saldo = 950
                    ),
                    PessoaJuridicaTable(
                        faturamento = 95682,
                        idade = 22,
                        nome_fantasia = "Macaco Louco",
                        celular = "(99) 44 6849-5568 ",
                        email_corporativo = "Macaco.Louco@company.com",
                        categoria = "Categoria C",
                        saldo = 15487
                    )
                    ]
                )
            ]
        )
    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass



def test_sacar_dinheiro():

    mock_connection = MockConnection()

    repo = PessoaJuridicaRepository(mock_connection)    

    response = repo.sacar_dinheiro("Roberto Company",20)

    mock_connection.session.query.assert_called_with(PessoaJuridicaTable)
    mock_connection.session.filter_by.assert_called_with(nome_fantasia = "Roberto Company")
    mock_connection.session.first.assert_called_once()
    mock_connection.session.update.assert_called_once()
    mock_connection.session.all.assert_not_called()

    
    assert "Valor" in response

def test_consultar_saldo():

    mock_connection = MockConnection()

    repo = PessoaJuridicaRepository(mock_connection)

    response = repo.consultar_saldo("Roberto Company")

    assert response == 950

    mock_connection.session.query.assert_called_with(PessoaJuridicaTable)
    mock_connection.session.filter_by.assert_called_with(nome_fantasia = "Roberto Company")
    mock_connection.session.first.assert_called_once()
    mock_connection.session.all.assert_not_called()

def test_realizar_extrato():

    mock_connection = MockConnection()

    repo = PessoaJuridicaRepository(mock_connection)

    response = repo.realizar_extrato("Roberto Company")

    mock_connection.session.query.assert_called_with(PessoaJuridicaTable)
    mock_connection.session.filter_by.assert_called_with(nome_fantasia = "Roberto Company")
    mock_connection.session.first.assert_called_once()
    
    assert isinstance(response, dict)

    assert response.get("Nome") == "Roberto Company"
    assert response.get("Saldo") == 950
    assert response.get("Categoria") == "Categoria B"

def test_criar_usuario():

    mock_connection = MockConnection()

    repo = PessoaJuridicaRepository(mock_connection)

    user = PessoaJuridicaAtributosInterface(
        faturamento= 159568,
        idade = 22,
        nome_fantasia = "Jesus Amado",
        celular= "(99) 54 95689-5487",
        email_corporativo= "Jesus@gmail.com",
        categoria= "Categoria SSS",
        saldo= 99999
        )

        
    repo.criar_usuario(user)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_listar_usuarios():

    mock_connection = MockConnection()

    repo = PessoaJuridicaRepository(mock_connection)

    response = repo.listar_usuarios()

    assert isinstance(response, list)

    mock_connection.session.query.assert_called_with(PessoaJuridicaTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.first.assert_not_called()
    mock_connection.session.filter.assert_not_called()
    mock_connection.session.filter_by.assert_not_called()