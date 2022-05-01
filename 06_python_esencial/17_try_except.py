def calcular_promedio(lista):
  assert len(lista)<0, "La lista esta vacia"
  return sum(lista)/len(lista)

try:
  promedio = calcular_promedio(lista=[])
  print(promedio)
except AssertionError as assert_error:
  print(assert_error)
except Exception as e: # para saber que tipo de error tengo
  print("La funcion no calculo el promedio")
  print(e)
# La lista esta vacia