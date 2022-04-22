from io import open # voy a utilizar la libreria io y su metodo open

# Creacion y apertura del fichero
fichero = open('archivo.txt', 'w') # el primer argumento es el nombre del archivo, el segundo argumento es el modo en que lo quiero abrir (w = write, escritura)
# La manipulacion del fichero
texto ='Hola Mundo\nEstoy estudiando Python'
fichero.write(texto) # como parametro paso el texto que va a tener
# El cierre del fichero
fichero.close() # siempre tengo que cerrar cuando tengo el metodo write