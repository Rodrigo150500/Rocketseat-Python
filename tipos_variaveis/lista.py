#Definção
minha_lista = [1,2,3,4,5, "rocketseat", True, False]

#Exibindo a minha lista
print(f"Minha lista: {minha_lista}")

#Exibindo os elementos
minha_lista[0] = "python"
print(f"minha_lista[0]: {minha_lista[0]}")
print(f"minha_lista[5]: {minha_lista[5]}")
print(f"minha_lista[1:7]: {minha_lista[1:7]}")
print(f"minha_lista[:6]: {minha_lista[:6]}")
print(f"minha_lista[2:]: {minha_lista[2:]}")


#Metodo append(): Adiciona um elemnto no final da lista
minha_lista.append(6)
print(f"\nApós append: {minha_lista}")

#Metodo index():
indice = minha_lista.index(6)
print(f"\nIndice do elemnto 6 é 8: {minha_lista[indice]}")

#Método insert: Adioina um elemento em um índice específico
minha_lista.insert(2, 10)
print(f"\nApós o insert (2, 10): {minha_lista}")

#Metodo pop()
elemento_removido = minha_lista.pop(3)
print(f"\nElemento removido: {elemento_removido}")
print(f"Após pop(3): {minha_lista}")

#Método remove()
minha_lista.remove(True)
print(f"\nApós remove(True): {minha_lista}")

#Método sort()
lista_desordem = [5,9,1,3,5,2]
lista_desordem.sort()
print(f"Após sort: {lista_desordem}")
