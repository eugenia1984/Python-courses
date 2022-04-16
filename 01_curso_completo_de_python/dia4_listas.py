# LISTAS
personas = ['Martin', 'Maria', 'Gonzalo', 'Raul','Pamela']
print(personas[0]) # accedo al indice 0, es decir el primer elemento
print(personas[3]) # accedo al indice 3, es decir el 4to elemento
print(personas[-1]) # accedo al ultimo elemento
print(personas[-2]) # accedo al anteultimo elemento
del personas[1] # con del elimino un elemento
print(personas) # se elimino el elemento con indicde ['Martin',  -> 'Gonzalo', 'Raul', 'Pamela']
personas.insert(0, 'Martina') # con .insert() agrego un elemento
print(personas)  # ['Martina', 'Martin', 'Gonzalo', 'Raul', 'Pamela'] asi agrego a Martina como primer elemento y desplazo todos un lugar
personas.append('Mateo')  # con .append agrego al final
print(personas) # ['Martina', 'Martin', 'Gonzalo', 'Raul', 'Pamela', 'Mateo']
listaMezclada = ['Martin', 10, True, ['Pyhton', 'Java', 'JavaScript'], 1.0]
print(listaMezclada) # ['Martin', 10, True, ['Pyhton', 'Java', 'JavaScript'], 1.0]
print(listaMezclada[3][0]) #Python