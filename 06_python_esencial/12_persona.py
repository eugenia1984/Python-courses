class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def cumplir_anios(self):
    self.edad += 1
    print(f"Feliz cumpleaños número {self.edad} {self.nombre}")

paco = Persona ('Paco', 20)
print(paco.cumplir_anios()) # Feliz cumpleaños numero 21 Paco