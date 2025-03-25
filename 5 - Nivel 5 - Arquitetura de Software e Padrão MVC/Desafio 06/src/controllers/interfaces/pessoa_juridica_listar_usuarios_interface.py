from abc import ABC, abstractmethod

class PessoaJuridicaListarUsuariosInterface(ABC):

    @abstractmethod
    def listar_usuarios(self) -> dict:
        pass
