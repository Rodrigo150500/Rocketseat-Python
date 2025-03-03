import pytest
from .pessoa_fisica_criar_usuario_controller import PessoaFisicaCriarUsuarioController
from src.models.sqlite.interface.pessoa_fisica_atributos_interface import PessoaFisicaInterface

class MockRepository:

    def criar_usuario(self, user_data: PessoaFisicaInterface) -> None:
        pass

    

def test_criar():

    mock_repository = MockRepository()

    controller = PessoaFisicaCriarUsuarioController(mock_repository)

    user = PessoaFisicaInterface(
        renda_mensal= 55.95,
        idade = 95,
        nome_completo = "Rodrigo Silva",
        celular = "+55 11 93658-6985",
        email = "rodrigo@gmail.com",
        categoria  = "Categoria A",
        saldo = 56.95
    )

    response = controller.criar(user)

    assert response['data']['type'] == "Pessoa Fisica"
    assert response['data']["count"] == 1
    assert response['data']["operation"] == "Criar Usuario"
    assert response['data']["atributes"] == {"nome": user.nome_completo, "idade":user.idade}

def test_criar_error():

    mock_repository = MockRepository()

    repo = PessoaFisicaCriarUsuarioController(mock_repository)

    person_info = {
        "renda_mensal" : "55.95",
        "idade" : 95,
        "nome_completo" : "Rodrigo Silva23",
        "celular" : "+55 11 93658-6985",
        "email" : "rodrigo@gmail.com",
        "categoria" : "Categoria A",
        "saldo" : "dfsd"
    }    

    with pytest.raises(Exception):
        repo.criar(person_info)