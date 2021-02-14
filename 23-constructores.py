# CONSTRUCTOR: una función que se ejecuta automáticamente al crear un nuevo objeto por medio de una clase.
# En este ejemplo es la parte de __init__

class Restaurant:

    def __init__(self, nombre):
      self.nombre = nombre  # atributo

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}') 

restaurant = Restaurant('Las Tercetas')   
restaurant.mostrar_informacion()

restaurant2 = Restaurant('El Cuartito')
restaurant2.mostrar_informacion()

# Ejemplo si agregamos má de un atributo, agregamos 'categoria'

class Restaurant:

    def __init__(self, nombre, categoria, precio):
      self.nombre = nombre  # atributo
      self.categoria = categoria #atributo
      self.precio = precio # atributo

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}') 

restaurant = Restaurant('Las Tercetas', 'pizzería', 'económico')   
restaurant.mostrar_informacion()

restaurant2 = Restaurant('El Cuartito', 'pizzería', 'intermedio')
restaurant2.mostrar_informacion()

"""
ABSTRACCION:
Son los DATOS necesarios de una CLASE.
Por ejemplo, si elaboras un menú de un restaurante es necesario el nombre del platillo, descripción y precio, otros datos como el color favorito dle chef no son necesarios.
"""