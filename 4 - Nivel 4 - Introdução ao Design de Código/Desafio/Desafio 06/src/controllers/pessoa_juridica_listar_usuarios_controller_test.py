from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from .pessoa_juridica_listar_usuarios_controller import PessoaJuridicaListarUsuarios

class MockRepository:
    def listar_usuarios(self) -> list[PessoaJuridicaTable]:
        return [PessoaJuridicaTable(
                    id = 1,
                    faturamento = 1500000.05,
                    idade = 2,
                    nome_fantasia = "Rodrigo Company",
                    celular = "(11) 95684-8445",
                    email_corporativo = "Rodrigo.company@company.com",
                    categoria = "Categoria S",
                    saldo = 25.855                
                ),
                PessoaJuridicaTable(
                    id = 2,
                    faturamento = 450000.65,
                    idade = 5,
                    nome_fantasia = "Martino Enterprise",
                    celular = "(66) 95684-1230",
                    email_corporativo = "Martino.enterprise@enterprise.com",
                    categoria = "Categoria SS+",
                    saldo = 3600549               
                )
                
                ]

def test_listar_usuarios_PJ():

    mock_repository = MockRepository()

    controller = PessoaJuridicaListarUsuarios(mock_repository)

    response = controller.listar_usuarios()

    assert isinstance(response, dict)
    assert response == {
        "data":{
            "type": "Pessoa Juridica",
            "count": 2,
            "operation": "listar usuarios",
            "atributes": [{"nome_fantasia": "Rodrigo Company", "idade":2},
                          {"nome_fantasia": "Martino Enterprise", "idade": 5}]
        }
    }
    