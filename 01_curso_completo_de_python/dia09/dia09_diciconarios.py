personas= {'Martin':'Martinez', 'Jose':'Alvarez', 'Maria':'Gomez'}
print(personas.get('Jose')) # #lvarez -> get busca el key para mostrar el value
print(personas.keys()) # dict_keys(['Martin', 'Jose', 'Maria'])
print(personas.values()) # dict_values(['Martinez', 'Alvarez', 'Gomez'])
print(personas.items()) # dict_items([('Martin', 'Martinez'), ('Jose', 'Alvarez'), ('Maria', 'Gomez')])
# con un FOR recorro todo el diccionario y voy imprmiendo cada par clave valor
for clave, valor in personas.items():
  print(clave, valor)
"""
Martin Martinez
Jose Alvarez
Maria Gomez
"""
personas.pop('Martin') # para eliminar la KEY con el valor indicado
print(personas) # no muestra a Martin, elimino tanto la clave como el valor
personas.clear() # me elimina todos los elementos
