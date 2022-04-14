x=30  #declaro la variable x y le asigno un dato numerico ocn valor 30
print(x)  # la imprimo: 30
nombre = "Maria Eugenia" # declaro otra variable que almacena un string
print(nombre)  # imprimo la variable: Maria Eugenia
x = x.__add__(10) # el metodo add , sumara lo que paso por parametro (10) y al tener el = le estoy reasignando el valor a x
print(x) #40
diccionario = {'uno': x, 'dos':x.__add__(10)}  # ['uno': 30, 'dos':40]
print(f"{nombre.title()} cuesta {diccionario['uno']} pesos y el otro libro {diccionario['dos']} pesos")

