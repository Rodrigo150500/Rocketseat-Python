from .pessoa_juridica_realizar_extrato_controller import PessoaJuridicaRealizarExtratoController


class MockPerson:
    def __init__(self, nome, saldo, categoria) -> None:
        self.nome_fantasia = nome
        self.saldo = saldo
        self.categoria = categoria

class MockRepository:

    def realizar_extrato(self, nome_pessoa: str):

        pessoa = MockPerson(nome_pessoa, 15.99, "Categoria A")
        
        return {
            "Nome": pessoa.nome_fantasia,
            "Saldo": pessoa.saldo,
            "Categoria": pessoa.categoria
        }


def test_realizar_extrato_PJ():

    mock_repository = MockRepository()

    controller = PessoaJuridicaRealizarExtratoController(mock_repository)

    response = controller.realizar_extrato("Rodrigo")

    assert isinstance(response, dict)
    expected_response = {
        'data': {
            'type': 'Pessoa Fisica',
            'count': 1,
            'operation': 'realizar extrato',
            'atributes': {
                'Nome': 'Rodrigo',
                 'Saldo': 15.99,
                  'Categoria': 'Categoria A'
                  }}}
    assert response == expected_response