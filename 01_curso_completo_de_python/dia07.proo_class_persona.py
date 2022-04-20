class Persona:
  def __init__(self, nombre, edad, sexo):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo

  def datosPersonales(self):
    print(f'El nombre de la persona es: {self.nombre}')
    print(f'La edad de la persona es: {self.edad}')
    print(f'El sexo de la persona es: {self.sexo}')

persona1 = Persona('Eugenia', 25, 'Femenino')
persona1.datosPersonales()