from src.models.sqlite.interface.pessoa_juridica_atributos_interface import PessoaJuridicaAtributosInterface
from .pessoa_juridica_criar_usuario_controller import PessoaJuridicaCriarUsuario

class MockPerson:
    def criar_usuario(self, user):
       pass


def test_criar_usuario_PJ():
    mock_repository = MockPerson()

    controller = PessoaJuridicaCriarUsuario(mock_repository)

    user = PessoaJuridicaAtributosInterface(
            faturamento=15900,
            idade=12,
            nome_fantasia="Mercado Company",
            celular= '(11) 5668-9855',
            email_corporativo="Mercado@company.com",
            categoria="Categoria S",
            saldo= 1500.22
        )

    response = controller.criar_usuario(user)

    expected_response = {
            "data":{
                "type": "Pessoa Fisica",
                "count": 1,
                "operation": "Criar Usuario",
                "atributes": {"nome_fantasia": user.nome_fantasia, "idade": user.idade}
            }
        }

    assert isinstance(response, dict)
    assert response == expected_response
