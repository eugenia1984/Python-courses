def calcular_promedio(lista):
  return sum(lista)/len(lista)

try:
  promedio = calcular_promedio(lista=[])
  print(promedio)
except:
  print("La funcion no calculo el promedio")
# La funcion no calculo el promedio

try:
  promedio = calcular_promedio(lista=[1, 2, 3])
  print(promedio)
except:
  print("La funcion no calculo el promedio")
# 2.0

try:
  promedio = calcular_promedio(lista=[])
  print(promedio)
except Exception as e: # para saber que tipo de error tengo
  print("La funcion no calculo el promedio")
  print(e)
# La funcion no calculo el promedio
# division by zero