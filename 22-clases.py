# Creando una clase y definiendo unos métodos

# El nombre de la clase va con la primer letra en mayúscula
# Agrego una FUNCIÓN, también llamada MÉTODO, es como una función, hay que declararla y mandar a llamar, lo que se llama INSTANCIAR LA CLASE

class Restaurant:

    def agregar_restaurant(self, nombre):
       self.nombre = nombre  # atributo

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}') 

# instanciar la clase(Restaurant) creando la variable restaurant
#Creo un primer objeto
restaurant = Restaurant()   
restaurant.agregar_restaurant('Las Tercetas')
restaurant.mostrar_informacion()

# Creo un segundo objeto
restaurant2 = Restaurant()
restaurant2.agregar_restaurant('El Cuartito')
restaurant2.mostrar_informacion()

# hay otra forma de mostrar la información
print(f'Nombre restaurant: {restaurant.nombre}')
print(f'Nombre restaurant: {restaurant2.nombre}')