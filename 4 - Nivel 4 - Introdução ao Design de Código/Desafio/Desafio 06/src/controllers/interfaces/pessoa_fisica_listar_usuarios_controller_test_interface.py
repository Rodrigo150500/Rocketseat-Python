from abc import ABC, abstractmethod

class PessoaFisicaListarUsuariosInterface(ABC):

    @abstractmethod
    def listar_usuarios(self) -> dict:
        pass
