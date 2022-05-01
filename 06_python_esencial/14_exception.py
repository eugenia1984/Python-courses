def validar_x(x):
  if x<1:
    raise Exception("La variable x debe ser mayor a 1")
  else:
    print("x es mayor a 1")

x = 0.3
validar_x(x) # Exception: La variable x debe ser mayor a 1
x = 2
validar_x(x) # x es mayor a 1