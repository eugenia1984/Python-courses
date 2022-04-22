nombreIngresado = input('ingrese su nombre por favor: ')
print('El nombre del usuario es: ', nombreIngresado)
# Metodo para pasar todo en mayuscula
print ('El nombre todo en mayuscula es: ', nombreIngresado.upper())
# Metodo para pasar todo en minuscula
print ('El nombre todo en minuscula es: ', nombreIngresado.lower())
# Si necesito la primer letra en mayuscula y el resto en minucula
print ('El nombre capitalizado es: ', nombreIngresado.capitalize())
mensaje = 'Hola mundo'
print(mensaje.isdigit()) # False, corrobora que no tengo un valor numerico
mensaje = '123'
print(mensaje.isdigit()) # True
numeroEntero = 123
"""
print(numeroEntero.isdigit()) 
# AttributeError: 'int' object has no attribute 'isdigit'
"""
segundoMensaje= 'Hola me llamo Eugenia'
print(segundoMensaje.split('-')) # ['Hola me llamo Eugenia']
print(segundoMensaje.split(' ')) # ['Hola', 'me', 'llamo', 'Eugenia']
print(segundoMensaje.isalnum()) # False busca si es alfanumerico