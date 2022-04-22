# Operadores relacionales
# Operador de igualdad : ==
c = "Raul" == "raul"
print(c) # False por ser case sensitive
# Operador Diferente que : !=
a = 10 != 20
print(a) # True porque no son iguales
#Operador menor que: <
caso1 = 5 < 4
print(caso1) # falso proque 5 no es menor que 4
# Operador mayor que : >
caso2 = 5 > 3
print(caso2) # True porque 5 es mayor a 3
# Operador menor o igual que: <=
caso3 = 20 <= 10
print(caso3) # False porque 20 no es menor ni igual a 10
# Operador mayor o igual que: >=
caso4 = 20 >=10
print(caso4) # True porque 20 es mayor a 10
# Operadores logicos
# NOT
print(not True) # False
print(not False) # True
# AND
print(True and False) # False
print(True and True) # True
# OR
print(True or False) # True
palabra = "Python"
#len(palabra) me da la longitud, la cantidad de caracteres que tengo
# con palabra[0] accedo al primer caracter
print(len(palabra)<8 or palabra[0] == "f") # True porque la longitud de palabra es menor a 8
# Operadores de asignacion
# Suma: +
numero1 = 10
numero1 +=10
print(numero1) # 20
# Resta: -
numero2 = 10
numero2 -=10
print(numero2) # 0
# Modulo : %
numero3 = 20
numero3 %= 2
print(numero3) # 0
# Division: /
numero4 = 30
numero4 /=5
print(numero4) # 6
# Potenciacion: **
numero5 = 2
numero5 **=3
print(numero5) # 8
# TAREA
# 1- Escriba un programa que lea dos numeros por teclado y determine con un valor booleano de True o False estos ejemplos:
# Si los dos numeros son iguales
primer_numero_ingresado = int(input("ingrese un primer numero entero: "))
segundo_numero_ingresado = int(input("Ingrese un segundo numero entero: "))
resultado1 = primer_numero_ingresado == segundo_numero_ingresado
print("Los dos numeros ingresados son iguales -> " , resultado1 )
# Si los dos numeros son diferentes
resultado2 = primer_numero_ingresado != segundo_numero_ingresado
print("Los dos numeros ingresados son diferentes -> " , resultado2)
# Si el primero es mayor que el segundo
resultado3 = primer_numero_ingresado > segundo_numero_ingresado
print("El primero es mayor que el segundo -> " , resultado3)
# Si el segundo es mayor o igual que el primero
resultado4 = segundo_numero_ingresado >= primer_numero_ingresado # tambien se puede poner como primer_numero_ingresado < segundo_numero_ingresado
print("El segundo es mayor o igual que el primero -> " , resultado4)
# 2- Conociendo los operadores logicos, realice una comprobacion si una cadena de texto ingresada desde teclado por el usuario tiene la longitud mayor o igual que 4 y a su vez que 7 (determinar con un valor booleano True o False)
cadena_ingresada = input("Ingrese una palabra: ")
longitud_palabra_ingresada= len(cadena_ingresada)
resultado5 = longitud_palabra_ingresada >= 4 and longitud_palabra_ingresada 
print("La cadena ingresada tiene la longitud mayor o igual que 4 y a su vez que 7 -> ", resultado5)
