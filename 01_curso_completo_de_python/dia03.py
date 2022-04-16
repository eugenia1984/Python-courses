# CONDICIONALES
# IF
edad = 20
if edad >=18:
  print("Es mayor de edad")
# IF ELSE
edadAEvaluar = 7
if edadAEvaluar >=18:
  print("Es mayor de edad")
else:
  print("Eres menor de edad")
# IF ELIF ELSE
edadActual = int (input("Escribe tu edad: "))
if edadActual >= 10 and edadActual <65:
  print('Eres Adulto')
elif edadActual >= 65:
  print('Eres adulto mayor') # si es mayor de 65 entra aca
else:
  print('Aun no eras adulto') #si es menor de 18 entra aca
# WHILE, EJEMPLO 1
edad2 = 1
while edad2 <=18:
  print("No eres mayor de edad todavía, tenes "+ str(edad2)+" años.")
  edad2+=4  # en cada iteracion del loop la variable edad2 va a ir incrementando de 4 en 4
# WHILE, EJEMPLO 2, CON LISTAS
lenguajes = ['Python', 'Java', 'C', 'JavaScript', 'Go']
lenguajeSeleccionado = 0
while lenguajeSeleccionado < len(lenguajes):
  print(lenguajes[lenguajeSeleccionado])
  lenguajeSeleccionado+=1
# BUCLE FOR
frutas = ['manzana', 'banana', 'uva', 'naranja']
for i in frutas:
  print(i)

for i in range(1,10):
  print(i)
# crea una lista del 1 al 10, incluido, el segundo parámetro dentro de range() no se incluye, por eso no se ve el 11  
# TAREA
# Ejercicio 1  : Escriba un programa que almacene la cadena de caracteres contraseña en una variable, para luego preguntarle al usuario por la contraseña. Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con la guardada en variable.
contraseniaGuardada = "123456"
contraseniaIngresada = (input("Ingrese la contraseña : "))
if contraseniaIngresada == contraseniaGuardada:
  print("Contraseña ingresada correctamente")
else:
  print("Error al ingresar la contraseña")
# Ejercicio 2 : Realice un programa que le pida al usuario dos números y muestre por consola su división. Si el divisor es cero el programa debe mostrar un error.
primerNumeroIngresado = int (input("Ingrese un numero: "))
segudoNumeroIngresado = int (input("Ingrese un segundo numero: "))
if segudoNumeroIngresado != 0:
  print(f"La division entre {primerNumeroIngresado} y {segudoNumeroIngresado} es : {primerNumeroIngresado/segudoNumeroIngresado}")
else:
  print("Error")
# Ejercicio 3 : Escriba un programa que le pida al usuario por teclado un numero entero y muestre en consola si es par o impar.
esParOImpar = int (input("Ingrese un numero: "))
if esParOImpar / 2 == 0:
  print("Ingreso un numero PAR")
else:
  print("Ingreso un numero IMPAR")

# Ejericicio 4 : Escriba un programa donde se evalué el ingreso a menores de edad, si la persona tiene menos de 19 años el programa le debe mostrar en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!
edadParaIngresar = int(input("Ingrese su edad para informarle si puede ingresar: "))
if edadParaIngresar >= 19:
  print("Bienvenido")
else:
  print("No puede ingresar")