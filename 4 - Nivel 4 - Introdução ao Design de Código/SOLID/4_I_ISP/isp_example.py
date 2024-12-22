from abc import ABC, abstractmethod

#PDF, TXT, EXCEL

#Nessa classe genérica temos todas as funções para os 3 tipos de arquivos, mas ao instanciar para um arquivo específico nota-se que não será necessário alguns métodos para sua aplicação
class Document(ABC):
    
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass


#Para deixar de forma coerente e que cada interface carregue consigo cada método para sua aplicação, vamos estar separando cada interface para cada aplicação

class DocumentPDF(ABC):

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

class DocumentTXT(ABC):

    @abstractmethod
    def load(self): 
        print("Carrengando arquivo PDF")

    @abstractmethod
    def view(self):
        print("Visualizando arquivo PDF")

class DocumentExcel(ABC):

    @abstractmethod
    def load(self):
        print("Carregando arquivo Excel")

    @abstractmethod
    def calculate(self):
        print("Calculando média")

class DocumenTXT(ABC):

    @abstractmethod
    def load(self):
        print("Carregando arquivo TXT")

    @abstractmethod
    def format(self):
        print("Formatando arquivo TXT")