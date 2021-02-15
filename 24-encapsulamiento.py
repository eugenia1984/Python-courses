# ENCAPSULAMIENTO: permite RESTRINGUIR u OCULTAR el acceso a los datos dentro de la misma clase del mundo exterior (usualmente se modifican vía métodos en la misma clase)

"""
Yo podría cambiar el precio reasignandole un nuevo valor, como hago en este ejemplo con restaurant.precio = 80

restaurant = Restaurant('Las Tercetas', 'pizzería', '50') 
print(restaurant.precio)  
restaurant.precio = 80
restaurant.mostrar_informacion()

Al encapsular evito que me modifiquen el precio

Por default están todas mis atributos:
self.nombre = nombre  
self.categoria = categoria 
self.precio = precio 

El PRECIO lo tengo que pasar a PROTECTED para que no me lo cambien, lo hago agregándole el _ y me queda ._precio

Para pasarlo  PRIVATE le hago doble guión bajo __ , pero al hacer esto no se va a poder acceder al atributo; sólo se va a apoder acceder por medio de un método: GET y SET.
"""

class Restaurant:

    def __init__(self, nombre, categoria, precio):
      self.nombre = nombre  
      self.categoria = categoria 
      self._precio = precio 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self._precio}') 

restaurant = Restaurant('Las Tercetas', 'pizzería', '50') 
print(restaurant._precio)  
restaurant.precio = 80
restaurant.mostrar_informacion()


restaurant2 = Restaurant('El Cuartito', 'pizzería', '60')
print(restaurant2._precio)  
restaurant2.mostrar_informacion()