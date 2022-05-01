from figuras.cuadrado import area_cuadrado, perimetro_cuadrado

lado = 5
cuadrado = {
  "lado": lado,
  "area": area_cuadrado(lado),
  "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado) # {'lado': 5, 'area': 25, 'perimetro': 20}