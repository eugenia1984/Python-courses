import pickle

"""
# Para modo en escritura binaria
lista = ['Maria', 'Pedro', 'Jose', 'Paola']
fichero = open('lista', 'wb') #wb escritura binaria
pickle.dump(lista, fichero)
fichero.close()
"""
fichero = open('lista', 'rb') #rb lectura binario
lista = pickle.load(fichero)
fichero.close()
print(lista) # ['Maria', 'Pedro', 'Jose', 'Paola']