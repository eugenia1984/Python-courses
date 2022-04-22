# 1 Escriba una función que muestre por consola un saludo personalizado. Por ejemplo ‘¡Hola mundo!’
from errno import EADDRNOTAVAIL
from mailbox import NoSuchMailboxError


def holaMundo():
  return print("Hola mundo!")
holaMundo()
# 2  Escriba una función que reciba un nombre por parámetro y que luego muestre en pantalla ¡Hola <nombre>!
def saludoPersonalizado(nombre):
  return print(f"Hola {nombre}")
saludoPersonalizado("Ana")
# 3 Cree una función que le pida el usuario su nombre y su edad, luego muestre en pantalla los resultados.
def mostrar():
  nombre = input("Ingrese su nombre: ")
  edad = input("ingrese su edad: ")
  return print(f"Ingreso : {nombre} , {edad}")
mostrar()
# 4 Definir una función que reciba dos números por parámetros y que luego los sume.
def suma(numero1, numero2):
  resultado = numero1 + numero2
  return print(f"la suma de {numero1} y {numero2} es: {resultado}")
suma(2,8)