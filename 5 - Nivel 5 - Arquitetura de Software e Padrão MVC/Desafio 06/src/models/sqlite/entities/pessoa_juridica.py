from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, BIGINT, REAL, String

class PessoaJuridicaTable(Base):

    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable= False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self) -> str:
        return f"Pessoa Juridica [nome_fantasia = {self.nome_fantasia}, idade = {self.idade}]"
    