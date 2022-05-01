from figuras.cuadrado import *
from figuras.circulo import *

lado = 4
cuadrado = {
  "lado": lado,
  "area": area_cuadrado(lado),
  "perimetro": perimetro_cuadrado(lado)
}

radio = 5
circulo = {
  "radio" : radio,
  "area" : area_circulo(radio),
  "perimetro": perimetro_circulo(radio)
}

print("Cuadrado: ", cuadrado) # Cuadrado:  {'lado': 4, 'area': 16, 'perimetro': 16}
print("Circulo: ", circulo) # Circulo:  {'radio': 5, 'area': 78.5, 'perimetro': 31.400000000000002}