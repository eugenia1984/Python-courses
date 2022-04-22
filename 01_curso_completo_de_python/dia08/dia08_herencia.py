# Creo la clase Persona
class Persona:
  def __init__(self, nombre, edad, apellido, sexo): # es el constructor
    self.nombre = nombre
    self.edad = edad
    self.apellido = apellido
    self.sexo = sexo

  def datosPersonales(self): # metodo que muestra todos los datos personales
    print(f'El nombre de la persona es: {self.nombre}')
    print(f'La edad de la persona es: {self.edad}')
    print(f'El apellido de la persona es: {self.apellido}')
    print(f'El sexo de la persona es: {self.sexo}')

## Creo la clase Empleado que hereda de persona
class Empleado(Persona):
  def datosEmpleado(self, vacaciones, salario):
    print(f'Sus dias de vacaciones son: {vacaciones}')
    print(f'Su salario es: {salario}')

miPersona = Persona('Raul', 22, 'Gonzalez', 'Masculino') # instancio un objeto de la clase persona
miPersona.datosPersonales()
print('*****************')
"""
El nombre de la persona es: Raul
La edad de la persona es: 22
El apellido de la persona es: Gonzalez
El sexo de la persona es: Masculino 
"""
# Instancio un empleado
miEmpleado = Empleado('Maria', 22, 'Torres', 'Femenino')
miEmpleado.datosPersonales()
"""
El nombre de la persona es: Raul
Le edad de la persona es: 22
El apellido de la persona es: Gonzalez
El sexo de la persona es: Masculino
"""
print('*****************')
miEmpleado.datosEmpleado(30, 80000)
"""
Sus dias de vacaciones son: 30
Su salario es: 80000
"""