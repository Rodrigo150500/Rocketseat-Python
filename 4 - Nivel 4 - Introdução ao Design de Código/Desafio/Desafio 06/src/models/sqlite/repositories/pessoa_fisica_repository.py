from src.models.sqlite.interface.cliente_interface import ClienteInterface
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from src.models.sqlite.interface.pessoa_fisica_atributos_interface import PessoaFisicaInterface
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from sqlalchemy.orm.exc import NoResultFound

class PessoaFisicaRepository(ClienteInterface, PessoaInterface):
    
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection


    def sacar_dinheiro(self, nome_pessoa_fisica: str, valor_sacar: float) -> dict:
        limite = 5000

        saldo = self.consultar_saldo(nome_pessoa_fisica)

        if valor_sacar > limite or valor_sacar > saldo:
            
            raise Exception("Saque inválido")
        else:
            
            saldo_remanescente = round(saldo - valor_sacar,2)

            with self.__db_connection as database:
                
                try:
                    database.session.query(PessoaFisicaTable).filter_by(nome_completo = nome_pessoa_fisica).update(
                        {"saldo":saldo_remanescente}
                    )

                    database.session.commit()

                    return {
                        "Nome": nome_pessoa_fisica,
                        "Saque": valor_sacar,
                        "Saldo": saldo_remanescente
                    }
                    

                except Exception as exception:
                    database.session.rollback()
                    raise exception

    def consultar_saldo(self, nome_pessoa: str) -> float:

        with self.__db_connection as database:

            try:

                consulta = database.session.query(PessoaFisicaTable).filter_by(nome_completo = nome_pessoa).first()

                saldo = consulta.saldo

                return saldo

            except NoResultFound:
                return 0
        

    def realizar_extrato(self, nome_pessoa_fisica: str) -> dict:
        try:
            with self.__db_connection as database:
                pessoa = (database.session
                            .query(PessoaFisicaTable)
                            .filter_by(nome_completo = nome_pessoa_fisica)
                            .first())

                extrato = {
                    "Nome": pessoa.nome_completo,
                    "Saldo": pessoa.saldo,
                    "Categoria": pessoa.categoria
                }

                return extrato

        except NoResultFound as exc:
            raise ValueError("Usuário não encontrado") from exc  # CORRETO

    def criar_usuario(self, user_data: PessoaFisicaInterface) -> None:

        user_data_table = PessoaFisicaTable(
            renda_mensal = user_data.renda_mensal,
            idade = user_data.idade,
            nome_completo = user_data.nome_completo,
            celular = user_data.celular,
            email = user_data.email,
            categoria = user_data.categoria,
            saldo = user_data.saldo
        )        

        try:
            with self.__db_connection as database:
                database.session.add(user_data_table)
                database.session.commit()

        except Exception as exception:
            database.session.rollback()
            raise exception

        
    def listar_usuarios(self) -> list[PessoaFisicaTable]:
        with self.__db_connection as database:

            try:
                users = database.session.query(PessoaFisicaTable).all()

                return users

            except NoResultFound:
                return []