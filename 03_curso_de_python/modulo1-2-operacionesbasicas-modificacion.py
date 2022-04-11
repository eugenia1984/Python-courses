# ¿Cual será la salida del siguiente programa?
x = 3
y = -2
y = x*y  # 3 x (-2) = -6
x = x**2  # 3 x 3 = 9
print(y)  # -6
print(x)  # 9

# ¿Cual será la salida del siguiente codigo?
x = 17
x = x + 3      # 17 + 3 = 20
x = x / 10     # 10 / 20 = 2
print(x)  # 2

# Mini-desafio: Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, y se muestre a la salida el promedio de los tres números.

primer_numero = float(input('Ingresa un primer número: '))
segundo_numero = float(input('Ingresa un segundo número: '))
tercer_numero = float(input('Ingresa un tercer nçumero: '))
promedio = float((primer_numero + segundo_numero + tercer_numero) / 3)
promedio_redondeado = round(promedio,2)
print(f'El promedio de los tres números ingresados es: {promedio_redondeado}')

"""
Ejemplos que encontré para redondear números con ROUND. Sino importando MATH con FLOOR y CEIL:

import math

numero = 1.4
redondeado = round(numero)
redondeado_abajo = math.floor(numero)
redondeado_arriba = math.ceil(numero)
print("Redondeado con round: {}".format(redondeado))
print("Redondeado con floor (hacia abajo): {}".format(redondeado_abajo))
print("Redondeado con ceil (hacia arriba): {}".format(redondeado_arriba))
"""

"""
OPERADOR MODULO: El operador módulo se utiliza con el símbolo %, y permite calcular el resto de un numero en la división por otro.

Ejemplo: Podríamos por ejemplo preguntar si el resto de un numero x en la division por y es igual a 0 y así saber si x es multiplo de y:
x = 20
y = 2
cuenta = x%y
print(cuenta)   # 0 por lo que x(20) es múltiplo de y (2)
"""

"""
Mini-desafio: Realizar un programa al cual se ingresa el día del año mediante un número de 0 a 364, y que muestra en pantalla a qué día de la semana corresponde mediante un número de 0 a 6 (mostrar el número 0 si corresponde a Lunes y 6 si es Domingo). Suponemos que el día 0 del año cae un Lunes.
"""
# Mediante un INPUT solicito ingrese el número, como queda STRING lo convierto a  número entero con INT
dia_ingresado = int(input('Por favor ingresa el día del año en número (entre 0 y 364): '))
# Con el módulo de 7 calculo el día ingresado
dia_semana = dia_ingresado%7
print(f'Tu día ingresado es: {dia_semana}, recordá que 0 es Lunes y 6 es Domingo')

