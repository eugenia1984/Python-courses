conjunto = set() # asi declaro al conjunto
conjunto = {2, 'Python', 2, 'Euge', False}
print(conjunto) # {False, 'Python', 2, 'Euge'}
conjunto.add('Martin') # agrega un elemento en un lugar aleatorio ya que el conjunto no es una coleccion ordenada
print(conjunto) # {False, 2, 'Martin', 'Python', 'Euge'}
conjunto.discard('Euge')
print(conjunto) # {False, 2, 'Martin', 'Python'}
print('Python' in conjunto)  # True asi veo si un elemento esta en el conjunto
print('Marcos' not in conjunto)  #  al negar de que esta me va a dar True, ya que Marcos no se encuentra
conjunto.clear() # para eliminar todos los elementos
print(conjunto)  # set()