# Declaro las funciones
def restar(num1, num2):
  return num1 - num2

def sumar(num1, num2):
  return num1 + num2

def multiplicar(num1, num2):
  try:
    return num1 * num2
  except ZeroDivisionError:
    print("ERROR. No se puede dividir por 0")
    return "Operacion no valida"
    
def dividir(num1, num2):
  return num1/num2

# Pido por consola los dos numeros para poder realizar las cuentas de las funciones
opcion1 = int(input("Introduce el primer valor: "))  
opcion2 = int(input("Introduce el segundo valor: "))  

operacion = input('Introduce la operacion a realizar --->\nsumar\nrestar\ndividir\nmultiplicar :')
operacion.lower # para pasar todo a minuscula

if operacion == "sumar":
  print(sumar(opcion1, opcion2))
elif operacion == "restar":
  print(restar(opcion1, opcion2))
elif operacion == "multiplicar":
  print(multiplicar(opcion1, opcion2))
elif operacion == "dividir":
  print(dividir(opcion1, opcion2))
else:
  print('ERROR OPCION NO VALIDA')