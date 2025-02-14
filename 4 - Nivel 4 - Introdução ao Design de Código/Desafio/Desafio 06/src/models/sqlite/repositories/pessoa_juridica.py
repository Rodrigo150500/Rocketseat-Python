from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.settings.connection import DBConnectionHandler 
from src.models.sqlite.interface.cliente_interface import Cliente
from src.models.sqlite.interface.pessoa_interface import PessoaInterface

from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable

class PessoaJuridicaLocal:
    
    def __init__(self) -> None:
            
        self.faturamento = float
        self.idade = int
        self.nome_fantasia = str
        self.celular = str
        self.email_corporativo = str
        self.categoria = str
        self.saldo = float

class PessoaJuridicaRepository(Cliente, PessoaInterface):

    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection
    
    def sacar_dinheiro(self, nome_pessoa_juridica: str, valor_sacar: float) -> str:
        valor_limite = 15000

        saldo = self.consultar_saldo(nome_pessoa_juridica)

        if saldo <= valor_sacar or valor_sacar >= valor_limite:
            raise Exception("Saque inválido")
        else:

            saldo -= round(valor_sacar,2)

            with self.__db_connection as database:

                database.session.query(PessoaJuridicaTable).filter_by(nome_fantasia = nome_pessoa_juridica).update(
                    {
                        "saldo": saldo
                    }    
                )

                database.session.commit()

            return f"Valor a sacar: {valor_sacar}\nSaldo na conta: {saldo}"            

    def consultar_saldo(self, nome_pessoa_juridica: str) -> float:
        
        with self.__db_connection as database:

            try:
                user = database.session.query(PessoaJuridicaTable).filter_by(nome_fantasia = nome_pessoa_juridica).first()
                
                saldo = user.saldo

                return saldo

            except NoResultFound:
                return 0


    def realizar_extrato(self, nome_pessoa_juridica: str) -> dict:

        with self.__db_connection as database:
            user = database.session.query(PessoaJuridicaTable).filter_by(nome_fantasia = nome_pessoa_juridica).first()

        extrato = {
                    "Nome": user.nome_fantasia,
                    "Saldo": user.saldo,
                    "Categoria": user.categoria
                }
        return extrato

    def criar_usuario(self, user: PessoaJuridicaLocal) -> None:
        user = PessoaJuridicaTable(
            faturamento = user.faturamento,
            idade = user.idade,
            nome_fantasia = user.nome_fantasia,
            celular = user.celular,
            email_corporativo = user.email_corporativo,
            categoria = user.categoria,
            saldo = user.saldo
        )

        with self.__db_connection as database:
            
            try:

                database.session.add(user)
                database.session.commit()
            
            except Exception as exception:
                database.session.rollback()
                raise exception

    def listar_usuarios(self) -> list[PessoaJuridicaTable]:
        
        with self.__db_connection as database:
            
            try:
                users = database.session.query(PessoaJuridicaTable).all()

                return users
            
            except NoResultFound:

                return []


