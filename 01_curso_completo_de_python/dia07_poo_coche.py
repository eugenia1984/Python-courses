class Coche:
  def __init__(self, marca, kilometros, anio):
    self.marca = marca
    self.kilometros = kilometros
    self.anio = anio
    print(f'Se ha crado un auto {self.marca}, con {self.kilometros} kilometros')

  def __del__(self):
    print(f'Se ha vendido el auto {self.marca}')

  def __str__(self):
    return 'El auto es un {}, tiene {} kilometros, y es del año {}'.format(self.marca, self.kilometros, self.anio)
# instancio un objeto
miCoche = Coche('Audi', 200, 1995)
print(str(miCoche))
del(miCoche)
