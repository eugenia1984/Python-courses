"""
Listas
- pueden tener distintos tipos de elementos
- puede tener elementos repetidos
- es una estructura ordenada
- se declaran entre corchetes
"""
lenguajes = ['python', 'java', 'golang']
listaVariada = [1, 2.5, 'python', 2.5]
programacion = [lenguajes, 'dedicacion', 'practica'] # asi tengo lista anidada
print(lenguajes)
print(listaVariada[0]) # 1 asi accedo al primer elmento de la lista
print(len(listaVariada)) # 4 asi veo la lingitud, la cantidad de elementos de la lista
print(listaVariada[-1]) # 2.5 accedo al ultimo elemento
print(listaVariada[0:2]) # [1, 2.5]
print(programacion) # [['python', 'java', 'golang'], 'dedicacion', 'practica'] 
print(programacion[0][1]) # java asi accedo a un elemento dentro de la lista dentro de la lista
# la lista es mutable, puedo modificar su valor
lenguajes[0] = "dart" # ['dart', 'java', 'golang']
print(lenguajes)
lenguajes.append("python") # append para agregar un elemento al final de la lista
print(lenguajes) # ['dart', 'java', 'golang', 'python']
otrosLenguajes = ['C', 'C++']
lenguajes.extend(otrosLenguajes) # extend une dos listas
print(lenguajes) # ['dart', 'java', 'golang', 'python', 'C', 'C++']
"""
Tuplas
- permiten almacenar elementos
- se definen entre () sus elementos se separan con coma
- es una estructura ordenada
- sus valores son inmutables, no podemos cambiar los valores que se designaron desde el inicio
"""
lenguajes2 = ('python', 'C', 'C++ ')
lenguajes3 = 'python', 'Java', 'Javascript' # python interpreta que es TUPLA ('python', 'Java', 'Javascript')
print(lenguajes3)
print(lenguajes3[0]) # para acceder al primer elemento : python
print(lenguajes3[-1]) # para acceder al ultimo elemento : JavaScript
"""
Diccionarios
- almacenan la informacion en pares de datos: key-value
- en otros lenguajes los diccionarios son conocidos como HashMap o JSON
- se definen entre {}
- sus elementos se separan con coma
- no se puede tener dos llaves iguales, son unicas
"""
diccionarioPython = { "nombre": "python", "creador": "Guido"}
print(diccionarioPython) # {'nombre': 'python', 'creador': 'Guido'}
# no se puede usar un indice para acceder a sus elementos, se usa la key
print(diccionarioPython["nombre"]) # python
# para añadir una nueva llave-valor
diccionarioPython["anio_lanzamiento"] = 1991
print(diccionarioPython) # {'nombre': 'python', 'creador': 'Guido', 'anio_lanzamiento': 1991}
diccionarioPython["anio_lanzamiento"] = 1999 # reasigno el valor, porque la llave es unica
print(diccionarioPython) # {'nombre': 'python', 'creador': 'Guido', 'anio_lanzamiento': 1999}
diccionarioPython["caracteristicas"] = ["sencillo", "facil", "genial"]
diccionarioPython.items() # retorna tuplas que tiene el par llave-valor
diccionarioPython.keys() # retorna la lista de las llaves
diccionarioPython.values() # retorna la lista de valores
"""
Sets
- tipo de estructura de datos que permiten guardar elementos unicos
- sus elmeentos se separan por comas
- no son estructuras ordenadas, por lo que no podemos acceder a ellos a través de los índices
- puede guardar todo tipo de elementos
- los elementos deben ser inmutables
"""
set1 = {1,2,3}
set2 = {1, 1, 1, 2, 3, 4}
print(set2) #{1, 2, 3}
set3 = {1, 2.0, "texto"}
# para añadir elementos al set utilizamos .add()
set1.add(4)
print(set1) # {1, 2, 3, 4}
# con .update() agregamos elementos
set1.update([4, 5, 6]) # {1, 2, 3, 4, 5, 6}
print(set1)
# con .len() averiguo la cantidad de elementos que tiene el set
print(len(set1)) # 6
# con .discard() elimino el elemento del set
set1.discard(2)
print(set1) # {1, 3, 4, 5, 6}
# con .removed() elimino elementos del set, el tema es que aca entre los () debo poner que elemento eliminar, y si pongo uno que no tiene Python da error
set1.remove(3)
print(set1) # {1, 4, 5, 6}
# con .clear() elimino todos los elementos del set
set2.clear()
print(set2) # set()

