#FUNCIONES: mostrasNombre(nombre)   vs   MÉTODOS: nombre.upper() -nombre de la función + . + método

#Defina una varaible y la asigno un valor
nombre3 = 'Jose'
#Creo la función 'mostrar_nombre' con el parámetro 'nombre3' que es mi varaible ya definida
def mostrar_nombre(nombre3):
  print(f'Hola {nombre3}')

mostrar_nombre(nombre3)

print( nombre3.upper() )   #ejemplo de método con nuestra variable + . + función (upper())