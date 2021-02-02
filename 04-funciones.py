#FUNCION: bloque de código para realizar una actividad. Primer paso: definir(crear) la función. Segundo paso: ejecutar la función. Ejemplo: def hola(parametro):

#Definimos la función:
def informacion():
  print('Hola')
#La mandamos a llamar:
informacion()

#Ejemplo de Función con dos parámetros:
def informacion(nombre, puesto='Desconocido'):
  print(f'soy {nombre} y soy {puesto}')

informacion('Pedro', 'Programador')
informacion('Itzel', 'Diseñadora')
informacion('Juan')

#Ejemplo de función que retorna en valor
def info(nombre2):
  return nombre2

empleado = info('Ana') #la variable EMPLEADO está asignada con lo que devuelve la función INFO con el parámetro ANA
print(empleado)





