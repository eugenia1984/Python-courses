from io import open # voy a utilizar la libreria io y su metodo open

# Creacion y apertura del fichero
fichero = open('archivo.txt', 'w') # el primer argumento es el nombre del archivo, el segundo argumento es el modo en que lo quiero abrir (w = write, escritura)
# La manipulacion del fichero
texto ='Hola Mundo\nEstoy estudiando Python'
fichero.write(texto) # como parametro paso el texto que va a tener
# El cierre del fichero
fichero.close() # siempre tengo que cerrar cuando tengo el metodo write

# Creo un segundo archivo en modo r(escritura)
fichero_read = open('archivo.txt', 'r')
texto2 = fichero_read.read()
fichero_read.close()
print(texto2)
print(texto2[0]) # H
"""
# Por consola veo:
Hola Mundo
Estoy estudiando Python
"""

fichero2 = open('archivo.txt', 'r')
linea = fichero2.readlines()
fichero2.close()
print(linea) # ['Hola Mundo\n', 'Estoy estudiando Python']
print(len(linea)) # 2
#print(linea(1)) # Estoy estudiando Python

fichero3 = open('archivo.txt', 'a')
fichero3.write('\nEste es el metodo append')
fichero3.close()
