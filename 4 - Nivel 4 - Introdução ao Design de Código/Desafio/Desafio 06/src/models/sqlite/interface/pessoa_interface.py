from abc import ABC, abstractmethod

class PessoaInterface(ABC):

    @abstractmethod
    def criar_usuario(self):
        pass

    @abstractmethod
    def listar_usuarios(self):
        pass