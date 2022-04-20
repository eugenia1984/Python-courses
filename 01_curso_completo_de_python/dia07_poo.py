from email.errors import StartBoundaryNotFoundDefect


class Gelatina:
  # es mi constructor, el self es como el this
  def __init__(self, sabor, color, tamanio):
      self.sabor = sabor
      self.color = color
      self.tamanio = tamanio

  # un metodo de la clase
  def imprimir(self):
    print(f'La gelatina es de {self.sabor}')
    print(f'La gelatina se ve de de {self.color}')
    print(f'La gelatina es de un tamaño {self.tamanio}')
# instancio la clase Gelatina para crear mi primer objeto    
gelatina1 = Gelatina('Frutilla', 'Rojo', 'Grande')
gelatina1.imprimir()  # invoco al metodo para imprimir
# instancio nuevamente la clase para crear otro objeto
gelatina2 = Gelatina('Pomelo', 'Naranja', 'Mediana')
gelatina2.imprimir()