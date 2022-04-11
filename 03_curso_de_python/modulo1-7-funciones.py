"""
#Ejemplo 1:

def suma(a,b):
    return a+b
z = suma(2,4)
print(z)           # 6

#Ejemplo 2:

#Defino la función:
def f_hola(x):
  y = x + 1 
  return y

r = f_hola(10)
print("La variable r tiene el valor: ",r)

#Ejemplo 3:
def chequarContraseña(c):
    if c == "Secreto":
        resultado = True
    else:
        resultado = False
    return resultado
        
print( chequarContraseña("hola") )  #False
print( chequarContraseña("Secreto") )  #True
"""  

"""
#MINI-DESAFIO FUNCIONES: Escribir una función que chequee los siguientes usuarios y contraseñas:
Usuario: Juan - Contraseña: 12345_
Usuario: Pablo - Contraseña: xDcFvGbHn
La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.
"""
def chequearUsuarioContraseña(usuario, contraseña):
  if (usuario == 'Juan' and contraseña == '12345_') or (usuario == 'Pablo' and contraseña == 'xDcFvGbHn'):
    return True
  else:
    return False

nombre = input('Ingrese su Usuario: ')
password = input('Ingrese su Contraseña: ')
print(chequearUsuarioContraseña(nombre, password))