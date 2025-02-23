from .pessoa_juridica_consultar_saldo_controller import PessoaJuridicaConsultarSaldoController


class MockRepository:
    def consultar_saldo(self, nome_fantasia) -> float:
        return 15


def test_consulta_saldo_controller_PJ():

    mockRepository = MockRepository()

    controller = PessoaJuridicaConsultarSaldoController(mockRepository)

    response = controller.consulta_saldo("Rodrigo Company")

    assert isinstance(response, dict)
    assert response['data']['type'] == "Pessoa Juridica"
    assert response['data']['count'] == 1
    assert response['data']['operation'] == "consulta saldo"
    assert response['data']['response'] == 15
