from .pessoa_fisica_listar_usuarios_controller import PessoaFisicaListarUsuariosController
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class MockRepository:

    def listar_usuarios(self):
        return [PessoaFisicaTable(
                id = 3,  
                renda_mensal = 6200.45,  
                idade = 38,  
                nome_completo = "Carlos Mendes",  
                celular = "+55 31 99876-5432",  
                email = "carlos.mendes@email.com",  
                categoria = "Categoria Gold",  
                saldo = 2100.75,  
        ),
        PessoaFisicaTable(
            id = 4,  
            renda_mensal = 8900.60,  
            idade = 50,  
            nome_completo = "Fernanda Oliveira",  
            celular = "+55 41 92345-6789",  
            email = "fernanda.oliveira@email.com",  
            categoria = "Categoria Diamante",  
            saldo = 4750.90,  
        )]


def test_listar_usuario():

    mock_repository = MockRepository()
    controller = PessoaFisicaListarUsuariosController(mock_repository)

    response = controller.listar_usuarios()

    expected_response = {
            "data":{
                "type": "Pessoa Fisica",
                "count": 2,
                "operation": "listar usuarios",
                'atributes': [{"nome_completo": "Carlos Mendes", "idade": 38}, {"nome_completo":"Fernanda Oliveira", "idade": 50}]
            }
        }


    assert isinstance(response, dict)
    assert response == expected_response