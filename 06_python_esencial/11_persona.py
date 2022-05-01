class Persona:
  atributo = 123

  def __init__(self, nombre, edad):
    """Funcion constructora"""
    self.nombre = nombre
    self.edad = edad

paco = Persona('Paco', 20)
print(paco.nombre) # Paco
print(paco.edad) # 20
print(paco.atributo) # 123