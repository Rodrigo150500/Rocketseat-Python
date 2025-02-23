from .pessoa_juridica_sacar_dinheiro_controller import PessoaJuridicaSacarDinheiroController


class MockRepository:

    def sacar_dinheiro(self, nome_fantasia, valor_saque):
        return {
            "Nome": nome_fantasia,
            "Saque": valor_saque,
            "Saldo": 150.99
        }

def test_saque_controller_PJ():
    
    repository = MockRepository()

    controller = PessoaJuridicaSacarDinheiroController(repository)

    user_info = {
        "nome": "Rodrigo Company",
        "saque": 155
    }

    response = controller.sacar(user_info)

    assert isinstance(response, dict)
    assert response['data']['type'] == "Pessoa Juridica"
    assert response['data']['count'] == 1
    assert response['data']['response']['Saque'] == 155
    assert response['data']['response']['Nome'] == "Rodrigo Company"
    
