conjunto = set()
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
print(conjunto) # {1, 2, 3}
conjunto.discard(1)
print(conjunto) # { 2, 3}
conjunto2 = conjunto.copy() # hago una copia del conjunto
print(conjunto2) # { 2, 3}
conjunto.clear() # elimina todos los elementos de los conjuntos
print(conjunto) # set()