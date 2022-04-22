lista = [1, 2, 3, 4, 5]
lista2 = [7, 8, 9]
lista.append(6) # agrego al final
print(lista) # [1, 2, 3, 4, 5, 6]
lista.extend(lista2) # para unir listas
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista.count(1)) # 1, veo cuantas veces tengo el 1 en mi lista
print(lista.index(1)) # 0 , para ver en que indice esta un elemento
lista.insert(2,0) # voy a agregar en el indice 2 al numero 0
print(lista) # [1, 2, 0, 3, 4, 5, 6, 7, 8, 9]
print(len(lista)) # 10
print(lista.pop()) # 9
lista.remove(0) # voy a eliminar el 0
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8]
lista.reverse() # me la da vuelta el ultimo elemento pasa a ser el primero,el anteultimo elemento pasa a ser el segundo y asi
print(lista) # [8, 7, 6, 5, 4, 3, 2, 1]
lista.sort() # los ordena de menor a mayor
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8]