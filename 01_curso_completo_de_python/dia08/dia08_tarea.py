# 1 - Realice una clase persona con sus atributos correspondientes, luego haga una clase empleado que herede los atributos de la clase Persona. Por último, cree un método de la clase empleado e instancie la clase.
class Persona():
  def __init__(self, nombre, apellido, edad, nacionalidad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.nacionalidad = nacionalidad

class Empleado(Persona):
  def __init__(self, nombre, apellido, edad, nacionalidad, estado):
    Persona.__init__(self, nombre, apellido, edad, nacionalidad)
    self.estado = estado

  def estaJubilado(estado):
    if (estado == True):
      print('Esta jubilado')
    else:
      print('Es un empeado activo, no se jubilo todavia')

empleado1 = Empleado('Ana', 'Gonzalez', 35, 'Peruana', True)
empleado1.estaJubilado()