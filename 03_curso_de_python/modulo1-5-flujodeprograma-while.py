# Estructura while

# Ejemplo 1: Imprimir del 101 al 121 y luego que se vena los mensajes:  'Termina el while'  y "Continuo con el resto del programa"
x = 100

while x <= 120:
  x = x + 1
  print(x)

print('Termina el while')
print("Continuo con el resto del programa")
"""
Como X inicializa en 100 es menor o igual a 120, entonces se incrementa en uno y se imprime el nuevo valor, por cada ciclio primero se corrobora que cumpla la condición de ser menor o igual a 120 y luego se le suma 1 e imprime
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
Termina el while
Continuo con el resto del programa
"""

# Es importante tener en cuenta que la condición se evalúa sólo al principio del loop


# Ejemplo 2:

nota = int( input('Ingrese un número del 1 al 10: ') )

condi1 = nota < 1 
condi2 = nota > 10
condi = condi1 or condi2 

while condi:
  print('Fuera de rango!')
  nota = int( input('Ingrese un número del 1 al 10: ') )
  condi1 = nota < 1 
  condi2 = nota > 10
  condi = condi1 or condi2

print("Nota ok")


# Ejemplo 3: para imprimir los numeros del 1 al 9
numero_a_imprimir = 1
while numero_a_imprimir < 10:
  print(numero_a_imprimir)
  numero_a_imprimir+=1

1
2
3
4
5
6
7
8
9


# MINO-DESAFIO IF Y WHILE: Implementar un programa que muestre la siguiente secuencia: 1, 2, 3, 4, 5, 4, 3, 2, 1, 0. Para un desafío mayor: Utilizar un solo while, un solo if y un solo else.

a=1
b=4

while b>=0:
  if a<=5:
    print(a)
    a+=1
  else:
    print(b)
    b-=1

