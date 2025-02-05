from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class MockConnection:

    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = [

                (           
                    [mock.call.query(PessoaFisicaTable)],
                    [PessoaFisicaTable(renda_mensal = 15000, 
                                        idade= 35,
                                        nome_completo = "Diguinho",
                                        celular = "(59) 91657-4878",
                                        email = "Diguinho@gmail.com",
                                        categoria = "Categoria B",
                                        saldo = 15.90),
                    PessoaFisicaTable(renda_mensal = 1674, 
                                        idade= 23,
                                        nome_completo = "Murilo",
                                        celular = "(45) 97845-4598",
                                        email = "Murilo@gmail.com",
                                        categoria = "Categoria A",
                                        saldo = 65.99)]
                )
            ]
        )
    
    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass




def test_listar_usuarios():
    mock_connection = MockConnection()

    repo = PessoaFisicaRepository(mock_connection)

    response = repo.listar_usuarios()

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].nome_completo == "Diguinho"