# 1 Cree una clase Persona con sus atributos correspondientes: nombre, edad, sexo, nacionalidad. Luego cree una instancia de la clase Persona.
class Persona:
  def __init__(self, nombre, edad, sexo, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.nacionalidad = nacionalidad
  
  def __str__(self):
    return f'La persona se llama {self.nombre}, tiene {self.edad} años, es de sexo {self.sexo} y es de nacionalidad {self.nacionalidad}'
persona1 = Persona('Eugenia', 37, 'Femenino', 'Argentina')
print(str(persona1))

# 2 Cree una clase Auto con sus atributos correspondientes: marca, modelo, año, color. Defina también un método, donde luego al instanciar la clase nos diga si el auto esta encendido o apagado.
class Auto:
  def __init__(self, marca, modelo, anio, color):
    self.marca = marca
    self.modelo = modelo
    self.anio = anio
    self.color = color
  
  def encender(self, encendemos):
    self.encendido = encendemos
    if(self.encendido):
      return "El auto esta encendido"
    else:
      return "El auto este apagado"

miAuto = Auto('Fiat', 'Uno', 2020, 'Azul')
print(miAuto.encender(True))