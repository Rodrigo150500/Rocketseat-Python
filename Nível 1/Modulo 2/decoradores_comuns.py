#classmethod - Acessa os atributos da classe
#staticmethod - Realiza função mas sem acessar os atributos da classe

class MinhaClasse:

  valor = 10

  def __init__(self, nome):
    self.nome = nome

  def metodo_instancia(self):
    return f"Meu nome é {self.nome}"

  @classmethod
  def metodo_classe(cls):
    return f"O nome verdadeiro é tenho {cls.valor}" 
  
  @staticmethod
  def metodo_estatico():
    return f"Modelo estático "
  
obj = MinhaClasse(nome = "Rodrigo")

print(obj.metodo_instancia())
print(obj.metodo_classe())
print(obj.metodo_estatico())


#Na seguinte classe podemos realizar o uso do classmethod para instanciar de forma indireta
class Carro:

  def __init__(self, marca, modelo, ano) -> None:
    self.modelo = modelo
    self.marca = marca
    self.ano = ano

  @classmethod
  def novo_carro(cls, config):
    jesus, legal, meu = config.split(",")
    return cls(meu, jesus, legal) #A ordem em que é retornada é a mesma que é instanciada

carro_amarelo = Carro.novo_carro("Toyota,Corolla,2021")
print(carro_amarelo.modelo)
print(carro_amarelo.marca)
print(carro_amarelo.ano)

class Matematica: #Realizando a chamada da classe sem instanciar

    @staticmethod
    def soma(a,b):
        return a + b
    
print(Matematica.soma(1,3))
