class Persona:
  pass

pedro = Persona()
print(type(pedro)) # <class '__main__.Persona'>

paco = Persona()
print(type(paco)) # <class '__main__.Persona'>

print(pedro == paco) # False, porque los objetos son de igual tipo pero cada uno ocupa un lugar diferente en la memoria de la computadora, por lo que no son el mismo objeto