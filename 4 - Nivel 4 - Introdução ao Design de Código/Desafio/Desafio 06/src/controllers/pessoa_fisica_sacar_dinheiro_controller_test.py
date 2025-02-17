from .pessoa_fisica_sacar_dinheiro_controller import PessoaFisicaSacarDinheiroController

class MockRepository:

    def sacar_dinheiro(self, nome_pessoa: str, valor_sacar: float) -> str:
        return {
                "Saque": valor_sacar,
                "Saldo": 0,
                "Nome": nome_pessoa
                }

def test_saque():

    mock_repository = MockRepository()

    controller = PessoaFisicaSacarDinheiroController(mock_repository)

    saque_info = {
        "nome_completo": "Rodrigo Issao",
        "saque": 45.95
    }

    response = controller.sacar(saque_info)

    assert response["data"]["type"] == "Pessoa Fisica"
    assert response["data"]["count"] == 1
    assert response["data"]["operation"] == "Saque"

    assert isinstance(response["data"]["response"], dict)

    assert response["data"]["response"]["Saque"] == 45.95
    assert response["data"]["response"]["Nome"] == 'Rodrigo Issao'


