playlist = {}  #Diccionario vacío
playlist['canciones'] = []  #lista de canciones

# Función principal:
def app():

    #Agregar playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('¿Cómo deseas nombrar a la playlist?\r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            # Ya tenemos un nombre, desactivemos el True
            agregar_playlist = False

            # Mandar a llamar la función para agregar canciones
            agregar_canciones()

def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
      #Preguntar al usaurio qué canción desea agregar
      nombre_playlist = playlist['nombre']      
      pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}. \r\n Si no quiere agregar más canciones ingrese X.\r\n'
      pregunta == 'Escribe "X" para dejar de agregar canciones \r\n'

      cancion = input(pregunta)
      if cancion == 'X' or cancion == 'x':
          #Dejar de agregar canciones
          agregar_cancion = False
          # Mostrar resumen de la playlist
          mostrar_resumen()
      else:
          #Agrega las canciones a la playlist
          playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist}\r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)
app()