from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
import pytest
from sqlalchemy.orm.exc import NoResultFound

class MockConnection:

    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = [

                (           
                    [mock.call.query(PessoaFisicaTable)],
                    [PessoaFisicaTable(renda_mensal = 15000, 
                                        idade= 35,
                                        nome_completo = "Rodrigo",
                                        celular = "(59) 91657-4878",
                                        email = "Rodrigo@gmail.com",
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


class MockConnectionNoResult:

    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_exception_no_result
    
    def __raise_exception_no_result(self, *args, **kwargs):
        raise NoResultFound("No result Found")
    
    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoAdd:

    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.add.side_effect = self.__raise_exception_no_adding
    
    def __raise_exception_no_adding(self, *args, **kwargs):
        raise Exception("No adding data")
    
    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_listar_usuarios():
    mock_connection = MockConnection()

    repo = PessoaFisicaRepository(mock_connection)

    response = repo.listar_usuarios()

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].nome_completo == "Rodrigo"
    assert response[1].nome_completo == "Murilo"

def test_listar_usuarios_error():
    mock_connection = MockConnectionNoResult()

    repo = PessoaFisicaRepository(mock_connection)

    response = repo.listar_usuarios()

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []


def test_sacar_dinheiro():

    mock_connection = MockConnection()

    repo = PessoaFisicaRepository(mock_connection)

    response = repo.sacar_dinheiro("Rodrigo", 15)

    mock_connection.session.query.assert_called_with(PessoaFisicaTable)
    mock_connection.session.filter_by.assert_called_with(nome_completo = "Rodrigo")
    mock_connection.session.update.assert_called_once()
    mock_connection.session.first.assert_called_once()

    assert "Valor" in response

def test_sacar_dinheiro_error():

    mock_connection = MockConnectionNoResult()

    repo = PessoaFisicaRepository(mock_connection)


    with pytest.raises(Exception):
        repo.sacar_dinheiro("Rodrigo", 15) 

    mock_connection.session.query.assert_called_with(PessoaFisicaTable)


    mock_connection.session.filter_by.assert_not_called()
    mock_connection.session.update.assert_not_called()
    mock_connection.session.first.assert_not_called()
    mock_connection.session.commit.assert_not_called()




def test_consultar_saldo():

    mock_connection = MockConnection()

    repo = PessoaFisicaRepository(mock_connection)

    response = repo.consultar_saldo("Murilo")

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter_by.assert_called_once_with(nome_completo = "Murilo")
    mock_connection.session.first.assert_called_once()

def test_consultar_saldo_error():

    mock_connection = MockConnectionNoResult()

    repo = PessoaFisicaRepository(mock_connection)

    response = repo.consultar_saldo("Murilo")

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter_by.assert_not_called(nome_completo = "Murilo")
    mock_connection.session.first.assert_not_called()

    assert response == 0

def test_consultar_saldo_error():

    mock_connection = MockConnection()

    repo = PessoaFisicaRepository(mock_connection)

    response = repo.consultar_saldo("Murilo")

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter_by.assert_called_once_with(nome_completo = "Murilo")
    mock_connection.session.first.assert_called_once()

def test_realizar_extrato():

    mock_connection = MockConnection()

    repo = PessoaFisicaRepository(mock_connection)

    response = repo.realizar_extrato("Murilo")

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter_by.assert_called_once_with(nome_completo = "Murilo")
    mock_connection.session.first.assert_called_once()
    mock_connection.session.all.assert_not_called()

    assert isinstance(response, dict)

def test_realizar_extrato_error():

    mock_connection = MockConnectionNoResult()

    repo = PessoaFisicaRepository(mock_connection)

    with pytest.raises(Exception):
        response = repo.realizar_extrato("Murilo")

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter_by.assert_not_called()
    mock_connection.session.first.assert_not_called()
    mock_connection.session.all.assert_not_called()



def test_criar_usuario():
    
 
    mock_connection = MockConnection()

    repo = PessoaFisicaRepository(mock_connection)

    user = {
        "renda_mensal": 6500,
        "idade":56,
        "nome_completo":"Sasuke Uchiha",
        "celular":"(99) 6854-6536",
        "email":"sasuke.uchiha@gmail.com",
        "categoria":"Categoria C",
        "saldo" : 9662.05
    }  

    repo.criar_usuario(user)

    added_user = mock_connection.session.add.call_args[0][0]

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

    assert isinstance(added_user, PessoaFisicaTable)
    
    assert added_user.renda_mensal == 6500
    assert added_user.idade == 56
    assert added_user.nome_completo == "Sasuke Uchiha"
    assert added_user.celular == "(99) 6854-6536"
    assert added_user.email == "sasuke.uchiha@gmail.com"
    assert added_user.categoria == "Categoria C"
    assert added_user.saldo == 9662.05

def test_criar_usuario_error():   
 
    mock_connection = MockConnectionNoAdd()

    repo = PessoaFisicaRepository(mock_connection)

    user = {
        "renda_mensal": 6500,
        "idade":56,
        "nome_completo":"Sasuke Uchiha",
        "celular":"(99) 6854-6536",
        "email":"sasuke.uchiha@gmail.com",
        "categoria":"Categoria C",
        "saldo" : 9662.05
    }  


    with pytest.raises(Exception):
        repo.criar_usuario(user)
    
    mock_connection.session.add.assert_called_once()
    mock_connection.session.rollback.assert_called_once()
    mock_connection.session.commit.assert_not_called()

    
    


"""

Método	Descrição	Exemplo
assert_called()	                Verifica se foi chamado pelo menos uma vez.	                            mock.method.assert_called()
assert_called_once()	        Verifica se foi chamado exatamente uma vez.	                            mock.method.assert_called_once()
assert_called_with(*args)	    Verifica se foi chamado pelo menos uma vez com os argumentos exatos.	mock.method.assert_called_with(10, "teste")
assert_called_once_with(*args)	Verifica se foi chamado exatamente uma vez com os argumentos exatos.	mock.method.assert_called_once_with(10, "teste")
assert_not_called()	            Verifica que o método nunca foi chamado.	                            mock.method.assert_not_called()
assert_any_call(*args)	        Verifica se foi chamado pelo menos uma vez com os argumentos dados.	    mock.method.assert_any_call(10, "teste")
call_count	                    Retorna o número de vezes que o método foi chamado.	                    assert mock.method.call_count == 2
mock_calls	                    Lista todas as chamadas feitas ao mock.	                                print(mock.method.mock_calls)
reset_mock()	                Reseta o histórico de chamadas do mock.	                                mock.method.reset_mock()
"""