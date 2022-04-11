# La estructura del for permite realizar una serie de acciones con una variable, que cambia su valor en cada repetición (iteración).


# Ejemplo 1: 

for i in range(1,10,1):
   print('Numero: ' + str(i))
print('Se corto el ciclo')
"""
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
Número: 6
Número: 7
Número: 8
Número: 9
Se cortó el ciclo
"""


# Ejemplo 2:
print("for y in [10,255,'fsdf',4,5,6]")
for y in [10,255,'fsdf',4,5,6]:
    print(y)
"""
10
255
fsdf
4
5
6
"""

# range(a,b,d) nos genera los valores desde a hasta b con incrementos de d, por ejemplo el siguiente codigo generara los numeros pares entre 0 y 10:

"""
# Ejemplo 1 de range:

for x in range(0,10,2):
    print(x)

0
2
4
6
8
"""
# Noten que el límite superior del rango nunca es incluído.


#Ejemplo 2 de range:
print("range(5):")
for z in range(5):
    print(z)
"""
0
1
2
3
4
5
"""
#el rango es desde 0 a 5, y va de 1 en 1 (step=1)

# Ejemplo 3 de range:
print("range(10, 15):")
for x in range(10, 15,2):
    print(x)
"""
10
12
14
"""

# MINI-DEAFIO FOR: Mostrar la siguiente secuencia de datos utilizando la instrucción for y la instrucción if: 0, 1, 4, 9, 16, 25, 6, 7, 8, 9
print("range (0,10):")
for x in range (0,10):
  if x <=5:
    print (x*x)
  else:
    print(x)



