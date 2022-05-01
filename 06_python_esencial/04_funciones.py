APELLIDO = "Costa" # variable global
def funcion():
  print("Mi primera funcion")
  nombre ="Maria Eugenia" # variable local
  print(nombre, APELLIDO)

def perimetro_cuadrado1(lado, unidades):
  """Calcular el perimetro de un cuadrado:"""
  perimetro = lado * 4
  print(f"El perimetro es {perimetro} {unidades}")

def perimetro_cuadrado2(lado): # funcion con return
  perimetro = lado *4
  return perimetro

def area_cuadrado(lado): # funcion con return
  area = lado * lado
  return area

def calcular_cuadrado_perimetro(lado):
  """Calcular el perimetro de un cuadrado:
  
  Esta funcion recibe el valor del lado de un cuadrado
  y a partir de este calcula y retorna su perimetro
  
  Args:
      lado (int): medida del lado del cuadrado

  Returns:
  perimetro (int): perimetro dle cuadrado
  """
  perimetro = lado *4
  area = lado * lado
  return area, perimetro

funcion() 
# Mi primera funcion
# Maria Eugenia Costa
perimetro_cuadrado1(4, "cm") # El perimetro es 16 cm
perimetro_cuadrado1(lado=20, unidades="metros") # El perimetro es 80 metros
# lado parametro
# 25 argumento
perimetro = perimetro_cuadrado2(lado=5)
area = area_cuadrado(lado=5)
print(f"Area: {area}, Perimetro: {perimetro}") # Area: 25, Perimetro: 20
area2, perimetro2 = calcular_cuadrado_perimetro(lado=5)
print(f"Area: {area}, Perimetro: {perimetro}") # Area: 25, Perimetro: 20
