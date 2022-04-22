from paquete_personas.datos_personas import *
from paquete_personas.empleado import *

persona1 = Persona('Maria', 22, 'Femenino')
persona1.datosPersonales()
"""
El nombre de la persona es: Maria
La edad de la persona es: 22
El sexo de la persona es: Femenino
"""
empleado1 = Empleado('Cocinera', 60000, 30)
empleado1.datosEmpleado()
"""
Su ocupacion es: Cocinera
Su salario es: 60000
Sus vacaciones son: 30
"""