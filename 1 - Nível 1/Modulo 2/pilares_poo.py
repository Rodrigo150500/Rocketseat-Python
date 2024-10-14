#Exemplo de Herança
#Na herança podemos utilizar classes pais para repassarem os mesmos atributos para seus filhos, como no exemplo abaixo, que a classe animal passa seus atributos para as classes cachorro e gato



print("Exemplo de Herança: ")

class Animal:
  
  def __init__(self, nome) -> None:
    self.nome = nome

  def andar(self):
    print(f"O {self.nome} andou")
  
  def emitir_som(self):
    pass


class Cachorro(Animal):
  def emitir_som(self):
    return "Au, au"


class Gato(Animal):
  def emitir_som(self):
    return "Miau"

#O polimorfismo é o compostamento da determinada classe se comportar de acordo com o contexto que está sendo utilizado, o classe Gato possui o método de emitir som com "Miau" mesmo que tenha herdado a classe animal
print("Exemplo de Polimorfismo")


dog = Cachorro(nome = "Rex")
cat = Gato(nome = "Felix")

animais = [dog, cat]

for animal in animais:
  print(f"O {animal.nome} faz: {animal.emitir_som()}")


#O encapsulamento é uma forma de segurança para que nenhum contexto de fora tenha acesso aos atributos de uma classe, ela fica disponível apenas os métodos da classe
print("Exemplo de Encapsulamento")

class ContaBancaria:
  def __init__(self, saldo) -> None:
    self.__saldo = saldo

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def consultarSaldo(self):
    return self.__saldo


conta = ContaBancaria(saldo = 1000)

print(f"Saldo disponível: {conta.consultarSaldo()}")
conta.depositar(valor = 500)
print(f"Saldo disponível: {conta.consultarSaldo()}")
conta.sacar(valor= 200)
print(f"Saldo disponível: {conta.consultarSaldo()}")
conta.sacar(2000)
print(f"Saldo disponível: {conta.consultarSaldo()}")


#Abstração é uma classe modeladora para criação de outras classes, nessa classe colocamos os métodos que as classes que herdam da abstrada devem conter, um exemplo, é se por acaso você tem um banco de dados e uma classe sem uma classe abstrata é que se houver uma mudança para outro banco de dados você terá que realizar uma nova classe só para esse novo banco de dados, se houver uma classe abstrata você precisaria apenas garatir que a classe desse banco tenha os mesmos métodos que a abstrata.

print("\nExemplo de classe abstrata")

from abc import ABC, abstractmethod

class Veiculo(ABC):

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass


class Carro(Veiculo):
  def __init__(self) -> None:
    pass

  def ligar(self):
    return "O carro foi ligado com a chave"

  def desligar(self):
    return "O carro foi desligado com a chave"

carro_amarelo = Carro()

print(carro_amarelo.ligar())
print(carro_amarelo.desligar())