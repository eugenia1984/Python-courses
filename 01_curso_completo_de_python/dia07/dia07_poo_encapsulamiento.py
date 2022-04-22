class Coche:
  def __init__(self, marca, kilometros, anio):
    self.__marca = marca  # con el doble guion bajo encapsulo el atributo marca, lo hago privado
    self.kilometros = kilometros
    self.anio = anio
    print(f'Se ha crado un auto {self.__marca}, con {self.kilometros} kilometros')

  def __str__(self):
    return 'El auto es un {}, tiene {} kilometros, y es del año {}'.format(self.__marca, self.kilometros, self.anio) 

miCoche1 = Coche('Audi', 222, 1992)
miCoche1.marca = 'Peogeot' # al estar encapsulado no puedo cambiar el atributo
print(str(miCoche1)) # me muestra Audi