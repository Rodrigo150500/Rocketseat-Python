#Poo - Programação Orientada a Objeto

#Classe é um grupo de objetos que contenham as mesmas características

#Classe exemplo

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


#objeto

pessoa1 = Pessoa("Rodrigo", 25)

print(pessoa1.saudar())

pessoa2 = Pessoa(nome = "Aline",idade = 30)

print(pessoa2.saudar())