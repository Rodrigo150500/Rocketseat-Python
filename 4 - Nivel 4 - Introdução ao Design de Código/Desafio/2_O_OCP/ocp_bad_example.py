'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''
from abc import ABC, abstractmethod

class AprovaExame(ABC):

    @abstractmethod
    def aprovarExame():
        pass

    @abstractmethod
    def solicitarExame():
        pass


class Exame:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo


class AprovaExameSangue(AprovaExame):

    def aprovarExame(self, exame: Exame):
        if self.aprovarExame(exame) == True:
            print("Exame aprovado")

    def solicitarExame(self, exame: Exame):
        pass

class AprovaExameRaioX(AprovaExame):

    def aprovarExame(self, exame: Exame):
        if self.aprovarExame(exame) == True:
            print("Exame aprovado")

    def solicitarExame(self, exame: Exame):
        pass

exame_sangue = Exame('sangue')
exame_raioX = Exame('raioX')

solicitar_exame_sangue = AprovaExameSangue(exame_sangue).aprovarExame()
solicitar_exame_raioX = AprovaExameRaioX(exame_raioX).aprovarExame()