from abc import ABC, abstractmethod
from src.models.sqlite.interface.pessoa_fisica_atributos_interface import PessoaFisicaInterface
from src.models.sqlite.interface.pessoa_juridica_atributos_interface import PessoaJuridicaAtributosInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaInterface(ABC):

    @abstractmethod
    def criar_usuario(self, user_data: PessoaFisicaInterface | PessoaJuridicaAtributosInterface) -> None:
        pass

    @abstractmethod
    def listar_usuarios(self) -> list[PessoaFisicaTable] | list[PessoaJuridicaTable]:
        pass