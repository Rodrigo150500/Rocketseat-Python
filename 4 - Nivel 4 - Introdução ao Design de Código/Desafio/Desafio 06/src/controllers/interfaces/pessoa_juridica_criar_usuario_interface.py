from abc import ABC, abstractmethod
from src.models.sqlite.interface.pessoa_juridica_atributos_interface import PessoaJuridicaAtributosInterface

class PessoaJuridicaCriarUsuarioInterface(ABC):

    @abstractmethod
    def criar_usuario(self, user_info: PessoaJuridicaAtributosInterface) -> dict:
        pass
