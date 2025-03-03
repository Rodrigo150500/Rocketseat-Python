from abc import ABC, abstractmethod


class PessoaFisicaCriarUsuarioInterface(ABC):

    @abstractmethod
    def criar(self, person_info: dict) -> dict:
        pass