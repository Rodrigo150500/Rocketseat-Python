from src.models.sqlite.interface.cliente_interface import Cliente
from src.models.sqlite.interface.pessoa_Interface import PessoaInterface
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from sqlalchemy.orm.exc import NoResultFound


class PessoaFisicaRepository(Cliente, PessoaInterface):
    
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection


    def sacar_dinheiro(self) -> str:
        pass
        
        

    def realizar_extrato(self, nome_pessoa_fisica: str) -> float:
        try:
            with self.__db_connection as database:
                consulta = (database.session
                            .query(PessoaFisica)
                            .filter_by(nome_completo = nome_pessoa_fisica)
                            .first())

                saldo = consulta.saldo

                return saldo

        except NoResultFound as exc:
            raise ValueError("Usuário não encontrado") from exc  # CORRETO

    def criar_usuario(self):
        pass

    def listar_usuarios(self):
        pass