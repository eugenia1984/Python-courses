# 1 Encuentra el error en la siguiente línea de código. Luego tendrás que crear una excepción para evitar que el programa se caiga. Además, debes explicarle al usuario que fue lo que sucedió y darle la solución.
#  valor = 10/0
def dividir():
  num1 = int(input("Ingrese un valor: "))
  num2 = int(input("Ingrese otro valor: "))
  try:
    return print(num1 / num2)
  except ZeroDivisionError:
    print("ERROR. No se puede dividir por 0")
    return "Operacion no valida"
dividir()

# 2 Encuentra el error en la siguiente línea de código. Luego tendrás que crear una excepción para evitar que el programa se caiga. Además, debes explicarle al usuario que fue lo que sucedió y darle la solución.
#  miLista = [1,2,3,4,5 ]
#  miLista [7]
miLista = [1,2,3,4,5]

def imprimirElemento():
  try:
    indice = int(input("Ingresa un numero, para mostrar un elemento de esta lista: 1,2,3,4,5 : "))
    return print(miLista[indice])
  except IndexError:
    print("Error, numero fuera del limite, debe ser entre 0 y 4")
imprimirElemento()