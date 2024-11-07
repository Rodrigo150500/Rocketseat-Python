print("Exemplo de captura de exceções")
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Erro de valor, digite um número")
except ZeroDivisionError as e:
    print(f"Erro de zero division: {e}")
except Exception as e:    
    print("Ocorreu um erro:", str(e))
else:
    print(f"O resultado é: {resultado}")
finally:
    print("Operação finalizada")