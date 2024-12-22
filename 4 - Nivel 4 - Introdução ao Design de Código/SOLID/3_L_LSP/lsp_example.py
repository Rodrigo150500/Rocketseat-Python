#Nessas classes podemos entender que independete de quem renato observa o método é o mesmo para qualquer animal, felino ou leao

class Animal:
    
    def comer(self):
        print("O animal está comendo.")

    def dormir(self):
        print("O animal está dormindo")

class Felino(Animal):

    def lambert(self):
        print("O felino Lambert está labendo")

class Leao(Felino):

    def rugir(self):
        print("O leão Rugby está rugindo")

class Pessoa:

    def observar(self, animal: Animal):
        animal.comer()

animal = Animal()
felino = Felino()

leao = Leao()


renato = Pessoa()

renato.observar(animal)
renato.observar(felino)
renato.observar(leao)