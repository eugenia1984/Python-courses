print("Hello world") 
# Variables objeto con valor, almacenado en memoria, que puede cambiar con el tiempo
# las variables se asignan con =
# Al declarar una variable no es requerido su tipo
nombre = "Eugenia" # es una variable que guarda un STRING
entero = 10 # numero entero -> int
decimal = 10.8 # dunmero decimal -> float el . como separados decimal
booleanaPositivo = True # boolean
booleanaNegativa= False # boolean
print(type(nombre)) # con type() veo el tipo de variable -> <class 'str'>
print(type(entero)) # <class 'int'>
print(type(decimal)) # <class 'float'>
print(type(booleanaPositivo)) # <class 'bool'>
print(type(booleanaNegativa)) # <class 'bool'>
# Operaciones basicas en Python
# Operadores matematicas 
# suma + 
print(2+3) # 5
# resta - 
print(10-3) # 7
# multiplicacion *
print(10*3) # 30.0 siempre es numero float
# division /
print(10/2) # 5
# modulo %
print(5%2) # 1 es el resto de la division
# potencia **
print(2**2) # 4
# con + tambien puedo concatenar textos
texto1 ="hola "
texto2=", como estas?"
print(texto1+texto2) #hola , como estas?
# con * podemos multiplicar un texto con un numero entero que nos da como resultado el texto repetido las veces que indique con el numero
print(texto1*2) # hola hola 
# Operador comparativo o relacional, da un resultado booleano
# > mayor que
print(1>2) # False
# < menor que
print(1<6) # true
# >= mayor o igual que
print(2>=1) # true
# <= menor o igual que
print( 1<=1) # true
# == igual que
print(1 == 1) # true
# != difernete que
print(1 != 1) # false
# == me permite comparar string
print("texto" == "texto") # true
# built-in function
# print()
# int() castea a entero
# float() castea a floar
# str() castea a string
# type() retorna el tipo de valor
# help() retorna la documentacion de la funcion, si entre los () no indico voy a ver todo
print(help(type))
