"""
Veamos un ejemplo clásico: Crear una función que calcule el factorial de un número. El factorial de un número  n  es el producto de todos los números entre  1  y  n . Se suele denotar con un signo de exclamación, de la siguiente forma:  n!=1⋅2⋅3⋅ ... ⋅n .
Solución sin recursión:

def f(n):
  resultado = 1
  for x in range(1, n+1):
    resultado *= x
  return resultado

print( f(5) )
"""

"""
La conjetura del Dr. Lothar
Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:

Si el numero es par, se debe dividir por  2 .
Si el numero es impar, se debe multiplicar por  3  y sumar  1 .
Este proceso se repite hasta llegar al numero  1  y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

Ejemplos:

Input: 6
Output: 8 (Los pasos a seguir son: 6, 3, 10, 5, 16, 8, 4, 2, 1)

Input: 13
Output: 9 (Los pasos a seguir son: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1)
"""

numero = int(print('Ingresa un número entero positivo: '))

while (numero>0):
  if (numero%2 == 0):
    numero = numero/2
    print(numero)
  else:
    numero = (numero*3)+1
    print(numero)