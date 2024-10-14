from random import randint


class Sistema:

    @staticmethod
    def verificarInput(msg, numeroInput = False):
        while True:
            try:
                if numeroInput:
                    escolha = int(input(msg))
                    return escolha
                else:
                    escolha = input(msg)
                    while escolha == "":
                        print("\nDigite um valor válido!")
                        escolha = input(msg)
                    return escolha
            except Exception as e:
                print("Digite um valor válido!")


class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if (self.__vida <= 0):
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = self.__nivel * randint(2,5)
        alvo.receber_ataque(dano)
        print(f"O {alvo.get_nome()} recebeu {dano} pontos de dano")

   

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo):
        dano = randint(self.get_nivel() * 2, self.get_nivel() * 5)
        alvo.receber_ataque(dano)
        print(f"O {self.get_nome()} usou a {self.__habilidade} e deu {dano} pontos de dano")


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

    def ataque_especial(self, alvo):
        dano = randint(self.__nivel * 2, self.__nivel * 5)
        alvo.receber_ataque(dano)
        print(f"O {self.get_nome()} usou a {self.__habilidade} e deu {dano} pontos de dano")




class Jogo(Sistema):
    #Classe para gerenciamento do jogo
    def __init__(self):
        self.heroi = Heroi(nome = "Heroi", vida=100, nivel=5, habilidade="Super Forca")
        self.inimigo = Inimigo(nome = "Morcego", vida = 50, nivel = 3, tipo = "Voador")

    def iniciar_jogo(self):

        print("Iniciando Batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("Exibindo Detalhes")
            print(f"\nHeroi\n{self.heroi.exibir_detalhes()}")
            print(f"\nInimigo\n{self.inimigo.exibir_detalhes()}")

            input("Pressione Enter para iniciar o combate...")
            escolha = self.verificarInput("1. Ataque normal\n2. Ataque especial\nOpção: ", True)

            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha == 2:
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Digite uma opção válida")
            
            if (self.inimigo.get_vida() > 0):
               self.inimigo.atacar(self.heroi) 


            

        if self.heroi.get_vida() <= 0:
            print("Você perdeu!")
        else:
            print("Você venceu!")

jogo = Jogo()
jogo.iniciar_jogo()



