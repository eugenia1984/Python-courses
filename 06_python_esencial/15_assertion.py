def calcular_promedio(lista):
  assert len(lista)>0, "La lista esta vacia"
  return sum(lista)/len(lista)

promedio = calcular_promedio(lista=()) # La lista esta vacia
promedio = calcular_promedio(lista=(1, 3, 5)) # no me da error
print(promedio) # 3.0