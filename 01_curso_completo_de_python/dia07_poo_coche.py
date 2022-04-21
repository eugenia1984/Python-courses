class Coche:
  def __init__(self, marca, kilometros, anio):
    self.marca = marca
    self.kilometros = kilometros
    self.anio = anio
    print(f'Se ha crado un auto {self.marca}, con {self.kilometros} kilometros')

  def arrancar(self, arrancamos):
    self.enmarcha = arrancamos
    if(self.enmarcha):
      return "El auto esta encendido"
    else:
      return "El auto este apagado"

  def __del__(self): # con este metodo elimino el coche
    print(f'Se ha vendido el auto {self.marca}')

  def __str__(self):
    return 'El auto es un {}, tiene {} kilometros, y es del año {}'.format(self.marca, self.kilometros, self.anio)
# instancio un objeto
miCoche = Coche('Audi', 200, 1995)
print(str(miCoche))
print(miCoche.arrancar(True)) # El auto esta encendido
del(miCoche) # lo elimino -> Se ha vendido el auto Audi
#instancio un nuevo objeto
miCoche2 = Coche('Audi', 222, 1990)
miCoche2.marca= 'Peugeot' # asi modifico un atributo del objeto
print(str(miCoche2)) # El auto es un Peugeot, tiene 222 kilometros, y es del año 1990
