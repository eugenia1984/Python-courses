# OBJETOS: es similar a un array(lista), te permite agrupar contenido de diferente tipo de datos en una sola variable. Se accede a un elemento de una LIST por medio de su índice, en un objeto se accede por medio de un KEY(llave). En Python se usa algo llamado DICCIONARIO.

# Creando un diccionario simple

cancion = {
    'artista' : 'Metallica', # llave y valor
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 2000
}

print(cancion)
print(cancion['artista'])   #acceder a los elementos del diccionario

# Mexclar con un string, hay que previamente asignarlo a una variable
artista = cancion['artista']
print(f'Estoy escuchando a: {artista}')

# Agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'   #como no existe el valor playlist lo crea
print(cancion)

# Reemplazar valor existente
cancion['cancion'] = 'Seek & Destroy'  #como ya existe el valor canción lo reemplaza
print(cancion)

# Eliminar un valor
del cancion['lanzamiento']
print(cancion)

# Otros ejemplos con diccionario:

# Iniciar un diccionario vació, supongamos creas un video juego y no tiene ni el nombre del jugador ni el puntaje
jugador = {}  #diccionario vacío
print(jugador)

# suponemos se une un jugador
jugador['nombre'] = 'Eugenia'
jugador['puntaje'] = 0
print(jugador)

# suponemos que el puntaje va incrementando
jugador['puntaje'] = 100
print(jugador)

# Acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))  # si solo dejo 'consola' me dice NON, al agregar 'No existe ese valor' personalizo el mensaje 

# Iterar en el diccionario (objeto)
for llave, valor in jugador.items():
    print(llave)
    print(valor)

# eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)
