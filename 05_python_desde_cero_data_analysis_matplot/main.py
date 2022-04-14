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
# BOOLEANS
resultado1= ( 2 == 1+1) and ( 2 < 8) # True and True
print(resultado1) #True
resultado2 = ( 2 == 1+1) and ( 2 == 8) # True and False
print(resultado2) # False
resultado3 = ( 2 < 1+1) and ( 2 == 8) # False and False
print(resultado3) # False
print(type(resultado1)) #bool
# COMPROBACION DE TIPO DE DATOS
print(-1, type(-1)) # -1, <class 'int'>
print(3.1415, type(3.1415)) # 1.1415, <class 'float'>
print("hola", type("hola")) # hola , <'str'>
print(True, type(True)) # True, 'bool'
print(None, type(None)) #None <class 'NoneType'>
# CONVERSION DE TIPOS: CASTEO DE NUMBER A STRING
num=2
print(type(num)) #  <class 'int'> 
num = str(num)
print(type(num)) # <class 'str'>
# conversion dinamica
print(int(2.1)) # castea a int (entero) : 2
print(int("2")) # castea a int(entero) : 2
print(int(True), int(False)) # castea a int (entero): 1 0
print(str(2)) # castea a string : 2
print(str(3.1415)) # castea a String : 3.1415
print(str(None)) #castea a String : None

