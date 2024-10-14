lista = [1, 2, 3, 4 ,5]

for elemento in lista:
    print(elemento)

tupla = (1, 2, 3, 4, 5)
for elemento in lista:
    print(elemento)


for index, pos in enumerate(lista):
    print(f"Index: {index}, Elemento: {pos}")

pessoa = {
    "nome": "Rodrigo",
    "sobrenome": "Takara",
    "idade": 30,
    "altura": 1.80,
    "peso": 80,
    "genero": "masculino"
}
print("For utilizando dicionario-chave")

for chave in pessoa.keys():
    print(chave)

print("\nFor utilizado dicionario-valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando chave-valor")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#range()
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numero = []

for numero in range(5):
    lista_numero.append(numero)
    
print(lista_numero)
for indice in range(0, len(lista_numero)):
    if(lista_numero[indice] == 3):
        lista_numero[indice] = 5
    else:
        lista_numero[indice] = 0
print(lista_numero)

#Enumerate

lista_enumerate = ["a", "b", "c", "d", "e", "f"]

for valor, indice in enumerate(lista_enumerate):
    print(f"Valor: {valor}, Indice: {indice}")

