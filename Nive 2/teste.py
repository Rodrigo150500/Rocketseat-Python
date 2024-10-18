lista =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

for posicao, item in enumerate(lista):
  print(posicao)
  if item == 'a':
    lista.remove(item)
  elif item == 'b':
    lista.remove(item)
  elif item == 'c':
    lista.remove(item)
  elif item == 'd':
    lista.remove(item)
  elif item == 'e':
    lista.remove(item)
  elif item == 'f':
    lista.remove(item)
  elif item == 'g':
    lista.remove(item)
  elif item == 'h':
    lista.remove(item)
  elif item == 'i':
    lista.remove(item)
  elif item == 'j':
    lista.remove(item)
  elif item == 'k':
    lista.remove(item)
  
  print(len(lista))
  
print(lista)