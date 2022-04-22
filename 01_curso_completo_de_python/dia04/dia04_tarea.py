# TAREA
# 1 Escriba un programa que almacene en una Lista los cursos que has cursado o los que te gustaría cursar en Udemy. Luego muestre la lista por consola.
listaDeCursos = ['JavaScriot desde cero', 'React con TypeScript', 'Python desde cero']
for i in listaDeCursos:
  print(i)

# 2 Escriba un programa que almacene personas en una lista, luego que le muestre por pantalla el mensaje de ‘Su nombre es ‘nombre’
listaDePersonas = ['Analia', 'Carlos', 'Agustin', 'Andres']
for i in listaDePersonas:
  print(f'Su nombre es {i}')

# 3 Escribir un programa que guarde en una variable un diccionario con los siguientes valores {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y muestre en consola el símbolo o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.
diccionarioDeMonedas =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisaElegida = input("Ingrese una divisa -en palabra, con la primer letra en mayuscula-: ")
if divisaElegida.title() in diccionarioDeMonedas:
    print(f'El simbolo  es: {diccionarioDeMonedas[divisaElegida.title()]}')
else:
  print("La divisa no se encuentra en el diccionario")

# 4  En una tupla coloque los siguientes valores: números enteros, decimales, String, colecciones. Luego muestre en consola.
tupla = (20, 14.5, 'Hello', [1, 2, 3, 4, 5])
print(tupla)