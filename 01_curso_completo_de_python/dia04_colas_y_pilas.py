# COLAS
fila = ['Jose', 'Maria', 'Raul', 'Paola'] # va a simular una fila del supermercado, hay 4 personas que hacen al cola, el primero es Jose
print(fila) # ['Jose', 'Maria', 'Raul', 'Paola']
fila.append('Romina')  # agrego un elemento al final -> ['Jose', 'Maria', 'Raul', 'Paola', 'Romina']
i = fila.pop(0) # elimina al ultimo de la fila si entre los parentesis no aclaro nada, pero la ponerle el 0 me elimina el primero
print(i) # Jose
print(f'Estan atendiendo a {i}')  # Estan atendiendo a Jose, con el format puedo concatenar un String con una varaible, es como el template literal de JS pero en este caso la variable va sin el $
print(fila) #  ['Maria', 'Raul', 'Paola', 'Romina']
# PILAS