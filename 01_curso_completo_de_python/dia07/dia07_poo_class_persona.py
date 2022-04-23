import pickle
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
persona2 = Persona('Maria', 30, 'Femenino')
persona3 = Persona('Jose', 18, 'Masculino')

listaPersonas = [persona1, persona2, persona3]

fichero = open('Personas', 'wb') # abro el fichero en modo de escritura binaria
pickle.dump(listaPersonas, fichero) # la paso como primer argumento que voy a codificar
fichero.close()
del(fichero)

ficheroLeer = open('Personas', 'rb')
miPersona = pickle.load(ficheroLeer)
ficheroLeer.close()

for i in miPersona: # con el for itero Persona por Persona
  # print(i) -> me muestra el espacio en memoria ->  <__main__.Persona object at 0x000001C352BBBDF0>
  print(i.datosPersonales())