# LIST (arrays/arreglos/list): permite agrupar diferente información en un sólo lugar (en una sola variable). Puede contener cualquier tipo de datos.

# Ejemplo de lista:
meses = ["Enero", "Febrero", "Marzo"]
# Acceder a un elemento de una rreglo o list:
meses[0]   #Enero, reordá que se inicia la cuenta desde la posición 0

lenguajes = ["Python", "Kotlin", "Java", "JavasScript"]
print(lenguajes)     #Imprimo la lista
print(lenguajes[0])   #Si quiero acceder a Python

lenguajes.sort()   #para ordenarlos alfabéticamente

# Ejemplo de combinación de string con list
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificar valores de un arreglo (list)
lenguajes[2] = 'PHP'  #Reemplaza el valor 2 por PHP

# Agregar  un elemento a un arreglo (list)
lenguajes.append('Ruby')   # Se agrega al final de todo

# 1er forma de eliminar un producto de un arreglo (list)
del lenguajes[1]     # Aclaro qué posición es la que quiero eliminar

# 2da forma de eliminar de un arreglo (list)
lenguajes.pop()   # Elimina el último elemento
lenguajes.pop(1)   # Elimina una posición específica

# Eliminar por nombre:
lengajes.remove('PHP')