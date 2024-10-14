def meu_decorador(func):
  def wrapper():
    print("Executando antes de ser chamada")
    func()
    print("Executando depois de ser chamada")
  return wrapper

@meu_decorador
def minha_funcao():
  print("Executando minha função")

minha_funcao()

class MeuDecoradorDeClasse():
  def __init__(self, func) -> None:
    self.func = func

  
  def __call__(self) -> None:
    print("Executando Meu Decorador de Classe antes de ser chamada")
    self.func()
    print("Executando Meu Decorador de Classe depois de ser chamada")

@MeuDecoradorDeClasse
def minha_segunda_funcao():
  print("Executando minha segunda função")

minha_segunda_funcao()


