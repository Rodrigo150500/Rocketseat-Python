from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.settings.connection import DBConnectionHandler 
from src.models.sqlite.interface.cliente_interface import Cliente
from src.models.sqlite.interface.pessoa_interface import PessoaInterface

from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable

class PessoaJuridicaRepository(Cliente, PessoaInterface):

    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection
    
    def sacar_dinheiro(self, nome_pessoa_juridica: str, valor_sacar: float) -> str:
        valor_limite = 15000

        saldo = self.consultar_saldo(nome_pessoa_juridica)

        if saldo <= valor_sacar or valor_sacar >= valor_limite:
            return "Saque inválido"
        else:

            saldo -= valor_sacar

            with self.__db_connection as database:

                database.session.query(PessoaJuridicaTable).filter_by(nome_fantasia = nome_pessoa_juridica).update(
                    {
                        "saldo": saldo
                    }    
                )

                database.session.commit()
            
            return f"Saque realizado com sucesso. Saldo disponível R${saldo}"

    def consultar_saldo(self, nome_pessoa_juridica: str) -> float:
        
        with self.__db_connection as database:

            try:
                user = database.session.query(PessoaJuridicaTable).filter_by(nome_fantasia = nome_pessoa_juridica).first()
                
                saldo = user.saldo

                return saldo

            except NoResultFound:
                return 0


    def realizar_extrato(self, nome_pessoa_juridica: str) -> dict:
        pass

    def criar_usuario(self, user_data: dict) -> None:
        pass

    def listar_usuarios(self) -> list[PessoaJuridicaTable]:
        pass


