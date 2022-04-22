lista = [1, 2, 3, 4, 5]
lista2 = [7, 8, 9]
lista.append(6) # agrego al final
print(lista) # [1, 2, 3, 4, 5, 6]
lista.extend(lista2) # para unir listas
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8, 9]