# Exemplo

def saudacao(nome):
    print(f"Ola {nome}, seja bem-vindo")

print("Chamando a função saudacao: ")
saudacao("Rodrigo")
saudacao("Aline")

# Função com retorno

def quadrado(numero):
    resultado = numero ** 2
    return resultado

print(f"\nChamando função quadrado(): {quadrado(5)}")

# Função com multiplos paramestro

def soma(numero1, numero2):
    resultado = (numero1 + numero2)
    return resultado

print("\nChamando a funçao soma()")
print(f"A soma do numero 20 com o numero 50 é: {soma(20,50)}")
