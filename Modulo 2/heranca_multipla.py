#Herança multipla é quando herdamos um objeto com mais de uma classe

class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  
  def emitir_som(self):
    pass

class Mamifero(Animal):
  
  def amamentar(self):
    return f"O {self.nome} está amamentando"

class Ave(Animal):

  def voar(self):
    return f"O {self.nome} está voando"

class Morcego(Mamifero, Ave):

  def emitir_som(self):
    return f"O {self.nome} está emitindo sons ultrassônicos"

morcego = Morcego(nome = "Batman")

print(morcego.emitir_som())
print(morcego.amamentar())
print(morcego.voar())