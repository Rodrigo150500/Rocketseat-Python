from typing import Dict

#A seguinte função deixa explicito de como deve ser a entrada dos parâmetros e qual a saída planejada
def sum(elem1: int, elem2: float) -> float:
    return elem1 + elem2

val = sum(5, 2.6)
print(val)

#Podemos definir os tipos de saída como Dicionarios, Listas ou tuplas
def add(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return {"Return": response}

val2 = add(5, 9.5)
print(val2)