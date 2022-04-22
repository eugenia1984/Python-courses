tupla = (11, 'Python', True, [1,2,3])
print(tupla) # (11, 'Python', True, [1, 2, 3])
print(tupla[0]) # 11 asi accedo a su elemento de indice 0, su primer elmento
print(tupla[1:]) # ('Python', True, [1, 2, 3]) acceso a los elementos desde el segundo elemento[]
print(tupla[3][2]) # 3
print(tupla.index(True)) # 2 asi busco en que indice se encuentra el elemento indicado(True)
print(tupla.count(11)) # 1 con .count() se cuantas veces tengo un elemento en una tupla (recordar que la tupla puede tener elementos repetidos)
print(len(tupla)) # 5 con len() se cuantos elementos tengo
print(len(tupla[4]))  # 3 asi veo la longitud de la lista dentro de la tupla, cuantos elementos tiene