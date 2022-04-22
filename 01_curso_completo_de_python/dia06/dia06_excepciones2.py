try:
  c = int(input("Ingrese un valor: "))
  c/0
except ValueError:
  print("Debe ingresar un numero, no puede dividir una cadena de caracteres con un numero")
except Exception as c:
  print(type(c).__name__)  # ZeroDivisionError
