class Empleado:
  def __init__(self, ocupacion, salario, vacaciones):
    self.ocupacion = ocupacion
    self.salario = salario
    self.vacaciones = vacaciones

  def datosEmpleado(self):
    print(f'Su ocupacion es: {self.ocupacion}')
    print(f'Su salario es: {self.salario}')
    print(f'Sus vacaciones son: {self.vacaciones}')