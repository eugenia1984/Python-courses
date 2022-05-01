class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def cumplir_anios(self):
    self.edad += 1
    print(f"Feliz cumpleaños número {self.edad} {self.nombre}")

class Empleado(Persona):
  """La clase Empleado extiende de Persona"""
  def __init__(self, horas_totales, nombre, edad):
    """con super() hereda lso atributos de la clase persona, si no esta voy a sobreescribir el metodo constructor y no heredo los atributos de la clase Padre"""
    super(Empleado, self).__init__(nombre, edad)
    self.horas_totales = horas_totales

  def trabajar(self, horas_trabajadas):
    self.horas_totales = horas_trabajadas
    print(f"Usted ha trabajado: {horas_trabajadas} horas")
    print("Horas totales: ", self.horas_totales)

paco = Empleado(nombre='Paco', edad=20, horas_totales=200)
print(paco.cumplir_anios()) # Feliz cumpleaños numero 21 Paco
print(paco.trabajar(horas_trabajadas=8)) 
# Usted ha trabajado: 8 horas
# Horas totales:  8