from .pessoa_fisica_realizar_extrato_controller import PessoaFisicaRealizarExtratoController


class MockConnection:

     def realizar_extrato(self, nome_pessoa: str) -> dict:
        
        return {
            'Nome':"Rodrigo Takara",
            'Saldo': 55.99,
            'Categoria':"Categoria SS"
            }
def test_realizar_extrato():

    repo = MockConnection()

    controller = PessoaFisicaRealizarExtratoController(repo)

    response = controller.realizar_extrato("Rodrigo Takara")

    assert isinstance(response, dict)    
    
    expected_response = {
        "data":{
                "type": "Pessoa Fisica",
                "count": 1,
                "operation": "realizar extrato",
                "atributes": {
                    "Nome": "Rodrigo Takara",
                    "Saldo": 55.99,
                    "Categoria": "Categoria SS"
                }
            }
            }
    assert response == expected_response