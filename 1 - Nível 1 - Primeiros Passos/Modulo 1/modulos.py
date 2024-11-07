print("Exemplo de importação de um módulo padrão:")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")

import meu_modulo

msg = meu_modulo.saudacao("Rodrigo")
resultado = meu_modulo.dobro(5)
print(msg, resultado)

from meu_modulo import saudacao, dobro

msg = saudacao("Aline")

print(msg)
print(dobro(5))