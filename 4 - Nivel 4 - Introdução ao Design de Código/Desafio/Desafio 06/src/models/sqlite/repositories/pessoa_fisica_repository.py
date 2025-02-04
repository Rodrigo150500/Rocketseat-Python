from src.models.sqlite.interface.cliente_interface import Cliente
from src.models.sqlite.interface.pessoa_interface import PessoaInterface
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from sqlalchemy.orm.exc import NoResultFound

class PessoaInterface:
    def __init__(self) -> None:
        self.renda_mensal = float
        self.idade = int
        self.nome_completo = str
        self.celular = str
        self.email = str
        self.categoria = str
        self.saldo = float

class PessoaFisicaRepository(Cliente, PessoaInterface):
    
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection


    def sacar_dinheiro(self, nome_pessoa_fisica: str, valor_sacar: float) -> str:
        limite = 5000

        saldo = self.consultar_saldo(nome_pessoa_fisica)

        if valor_sacar > limite or valor_sacar > saldo:
            
            raise Exception("Saque inválido")
        else:
            
            valor_sacado = round(saldo - valor_sacar,2)

            with self.__db_connection as database:
                
                try:
                    database.session.query(PessoaFisicaTable).filter_by(nome_completo = "Rodrigo").update(
                        {"saldo":valor_sacado}
                    )

                    database.session.commit()
                    
                    return f"Valor a sacar: {valor_sacar}\nSaldo na conta: {valor_sacado}"

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

    def criar_usuario(self, user_data: PessoaInterface) -> None:

        user_data = PessoaFisicaTable(
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
                database.session.add(user_data)
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