# IF ELIF ELSE
# Primer ejemplo
from xml.dom.expatbuilder import FilterVisibilityController


a = 1
b = 2
if a>b:
  print("A es menor que B")
elif a==b:
  print("A es igual que B")
else:
  print("A es mayor que B")
# Segundo ejemplo con valores boleanos
esVerdadero = True

if esVerdadero:
  print("Es verdadero")
else:
  print("Es falso")
# Tercer ejemplo utilizando type() y is
if type(esVerdadero) is bool:
  print("Es booleano")
else:
  print("No es booleano")
# Cuarto ejemplo con AND
diez = 10
cinco = 5
uno = 1

if diez>cinco and cinco>uno:
  print("Las dos condiciones son verdaderas")
# Quinto ejemplo con OR
if diez>cinco or cinco>uno:
  print("Al menos alguna condicion es verdadera")
# CICLO FOR
# Iterar sobre un String, cada caracter es un elemento
for letra in "texto":
  print(letra)
"""
t
e
x
t
o
"""
# Iterar en un diccionario
lenguajes = ['python', 'java', 'goland']
for elemento in lenguajes:
  print(elemento)
"""
python
java
goland
"""
# Para modificar el flujo del ciclo con BREAK
for elemento in lenguajes:
  print(elemento)
  if elemento == "java":
    break
# solo se imprime python y java, por el BREAK
# Para modificar el flujo del ciclo con CONTINUE; para pasar al sigueinte elemento de la lista
for elemento in lenguajes:
  if elemento == "java":
    continue
  print(elemento)
"""
python
goland
"""
# Con RANGE podemos iterar sobre una lista de numeros consecutivos
for element in range(5):
  print(element)
"""
0
1
2
3
4
"""
# con dos parametros le indico el punto de partida y el de finalizacion, no incluye el ultimo numero
for element in range(1, 5):
  print(element)
"""
0
1
2
3
4
"""
# CICLO WHILE, tiene un contador para saber hasta cuando ejercer el ciclo
i = 1
while i <= 5:
  print(i)
  i+=1
# siempre debo modificar el i (indice / contador) sino me quedo en un ciclo infinito
contador = 1
while contador <= 5:
  print(contador)
  contador+=1
  if contador == 3: # Con una condicion para romper el ciclo
    break
"""
1
2
"""
# Iterando sobre una lista en Python
# con FOR, iterando sobre la lista
lenguajes = ['python', 'java', 'javascript']
for elemento in lenguajes:
  print(elemento)
# con los INDICES
for index in range(len(lenguajes)):
  print("indice", index)
  print("elemento", lenguajes[index])
# con WHILE, necesito el contador
i = 0
while i < len(lenguajes):
  print(lenguajes[i])
  i+=1
# Iterando sobre un diccionario
# usando FOR vamos a tener las llaves
lenguaje = {
  "nombre": "python",
  "creador": "Guido Van Rossum"
}

for llave in lenguaje:
  print("llave:", llave)
  print("valor:", lenguaje[llave])
"""
llave: nombre
valor: python
llave: creador
valor: Guido Van Rossum
"""
# utilizando keys
for elmento in lenguaje.keys():
  print(elemento)
"""
nombre
valor
"""
# utilizando values
for elmento in lenguaje.values():
  print(elemento)
"""
python
Guido Van Rossum
"""
# utilizando items, que me retorna dos valores llave, valor
for llave, valor in lenguaje.items():
  print(llave, valor)
"""
nombre python
creador Guido Van Rossum
"""
for elemento in lenguaje.items():
  print(elemento)
"""
('nombre' 'python')
('creador' 'Guido Van Rossum')
"""




