# ¿Cual será la salida del siguiente programa?

x = 5
y = 7
 
if x == y:
  print(x, " x es igual a y")
else: 
  print("fdfafdfa")   #sale fdfafdfa porque no cumple la condición x==y entonces ejecuta el else

"""
Ejemplo de IF / ELSE:
x = -1
y = 4

if y == 5:
    print("Adivinamos el valor de y!") 
else:
    print("No adivinamos el valor de x  :(")  

Ejemplo de IF / ELIF / ELSE:
x = -1
y = 4
if x > y:
    print("x es mayor que y")
elif x < y:
    print("y es mayor que x")
elif x == y:
    print("x e y son iguales")
else:
    print("que?????")
    """
# MINI DESAFIO IF - 1 : Realizar un programa que revise si una nota está aprobada (es decir si es mayor o igual a 4) utilizando un if/else. La nota será ingresada por el usuario usando input().

#Con INPUT pido que ingrese una nota y convierto el dato a número con INT, la guardo en la variable NOTA
nota = int(input('Por favor ingresa tu nota, para informate si estas aprobado/a: '))

#Si cumple la condición de IF (si la nota es mayor o igual a 4) está aprobado/a, sino va a ELSe y se informa que no está aprobado/a
if nota >= 4:
  print('Felicitaciones estás aprobado/a')
else:
  print('Lamentablemente no estás aprobado/a')

# MINI-DESAFIO IF - 2 : Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F de acuerdo a la siguiente conversión: A: 90-100 , B: 80-89 , C: 70-79, D: 60-69, F: 0-59

#Con INPUT se solicita ingrese una nota del 0 al 100, con INT se pasa a INTEGER y se guarda en la variable NOTA

nota = int(input('Por favor ingresa tu nota obtenida entre 0 a 100: '))

if nota>=90 and nota<100:
  print('Tu nota es A')
elif nota>=80 and nota <90:
  print('Tu nota es B')
elif nota>=70 and nota <80:
  print('Tu nota es C')
elif nota >= 60 and nota < 70:
  print('Tu nota es D')
else:
  print('Tu nota es F')

