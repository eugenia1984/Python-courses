x=30  #declaro la variable x y le asigno un dato numerico ocn valor 30
print(x)  # la imprimo: 30
nombre = "Maria Eugenia" # declaro otra variable que almacena un string
print(nombre)  # imprimo la variable: Maria Eugenia
x = x.__add__(10) # el metodo add , sumara lo que paso por parametro (10) y al tener el = le estoy reasignando el valor a x
print(x) #40
diccionario = {'uno': x, 'dos':x.__add__(10)}  # ['uno': 30, 'dos':40]
print(f"{nombre.title()} cuesta {diccionario['uno']} pesos y el otro libro {diccionario['dos']} pesos")
# Tipos de datos numericos
numero_entero = 2
print(type(numero_entero))
numero_decimal = 3.4
print(type(numero_decimal))
c = 1+2j # numero imaginario
print(type(c))
parte_real = c.real
parte_imaginaria = c.imag
print(parte_real)
print(parte_imaginaria)
# STRING
nombre = " Martina"
print(nombre) # Martina
print(type(nombre))
print("una cadena  \tseparada por una tabulacion") # Para tabular, dejar un espacio
print("una linea  \notra linea") # para un salto de linea
print(r"hola/mundo") # para mostrarlo en crudo
print(""" Primer linea
segunda linea
tercer linea""")
# BOOLEAN
print(1+1 == 2) #True
print( 3 < 1) # False

