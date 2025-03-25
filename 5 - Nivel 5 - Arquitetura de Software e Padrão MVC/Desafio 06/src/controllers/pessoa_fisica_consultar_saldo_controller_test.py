from .pessoa_fisica_consultar_saldo_controller import PessoaFisicaConsultarSaldoController

class MockRepository:

    def consultar_saldo(self, nome_pessoa: str) -> float:
        return 15

def test_consultar_saldo():

    mock_connection = MockRepository()
    controller = PessoaFisicaConsultarSaldoController(mock_connection)

    nome = "Rodrigo"

    response = controller.consulta_saldo(nome)

    assert isinstance(response, dict)
    assert response['data']['type'] == "Pessoa Fisica"
    assert response['data']['count'] == 1
    assert response['data']['operation'] == 'consulta saldo'
    assert response['data']['response'] == 15