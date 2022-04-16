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