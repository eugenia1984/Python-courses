# :book: Curso completo de Python. Desde 0 hasta Proyectos con Django (Alvarou Chirou y Brian De Vita - Udemy)

Temas a ver:

* Python desde 0. Ejercicios para materializar lo aprendido
* Script
* Framework Django
* Desarrollo de una App con Python
* Modelos y migraciones
* Bases de Datos
* Interfaces Graficas
* Manejo de vistas con clases
* Manipular API de Facebook
* Boostrap basico
* Html basico
* Usar Json
* Templates
* Modelos

---
---

 # :star: Día 1

Temas:

- Instalacion de Python

- Números y variables

- Textos

- Entrada desde teclado

- Instalación de VSC y conociendo a VSC

---

## :book: Instalacion de Python

Desde [http:/www.python.org](http:/www.python.org) se descarga e instala Python.

---

## :book: Numeros y variables

**Numeros Enteros**  -> **int**

**Numeros Flotantes** -> **float**, por ejemplo: 1.5. Se separan por . en vez de por coma.

**variable** -> espacio en memoria, como una caja, a la cual le guardamos un valor. Es Case sensitive, hay que tener esto en cuenta al asignarle un identificador. Es variable, porque durante el transcurso del programa el valor de la variable puede ser modificado.

Para declarar la variable directamente le doy un nombre

Para asignarle un valor utilizo **=**

Por ejemplo: 
```Python
i = 10
i = i + 20 # i = 30
division = i /30
resta = i - 2
multiplicacion = i *2
potenciacion = i **3
```

---

## :book: Textos (String)

```Python
print("Estoy 'aprendiendo' Python")
nombre="Maria Eugenia"
print("Buenas "+nombre) # para concatenar un String con una variable -> +
# con \t tabulo y con \n hago salto de linea
```

---

## :book: Input

```Python
entrada1 = input ("Introduce un numero : ") # va a entrar como String
```
Como entra como String es recomendable pasarlo a **int**:

```Python
entrada2 = int(input ("Introduce un numero : ")) # va a entrar como String y se castea a int
```
También puedo castearlo a **float**
```Python
entrada3 = float(input ("Introduce un numero decimal: ")) # va a entrar como String y se castea a int
```

---

## :book: Visual Studio Code

Desde [http://www.code.visuastudio.com](http://www.code.visuastudio.com) descargo Visual Studio Code y le agrego la extension de Python de Microsoft.

Dejar configurado que se vaya autoguardando lo que escribimos.

Todos los archivos que se creeen deben tener la extension **.py**

---

## Tarea

- 1- Escribir un programa que muestre por pantalla la cadena Hola mundo!

```Python
saludo = "Hola mundo!"
print(saludo)
```

- 2- Escribir un programa que guarde en variable la cadena Estoy aprendiendo Python! Y que luego muestre en pantalla el valor de la variable

```Python
aprendiendo = "Estoy aprendiendo Python!"
print(aprendiendo)
```

- 3- Escriba un programa que le pregunte al usuario su nombre para luego saludarlo por consola con su nombre

```Python
nombre_ingresado = input("Ingresa tu nombre: ")
print("Hola " + nombre_ingresado)
```

- 4- Defina tres variables: una que reciba un valor flotante, un valor entero y un String

```Python
calor_flotante = 15.67
valor_entero = 10
valor_cadena = "Estamos en feriado"
```

---
---

# :star: Dia 2

Temas

- El tipo logico

- Operadores Relacionales

- Operadores logicos

- Operadores de asignacion

---

## El tipo logico

**True** -> es verdad / 1

**False** -> es falso / 0

---

## Operadores

| aritmeticos | relacionales | logicos | asignacion |
| ----------- | ------------ | ------- | ---------- |
| SUMA + | IGUAL QUE == | AND | ASIGNACION = |
| RESTA - | MAYOR QUE > | OR | DECREMENTO -= o INCREMENTO +=|
| MULTIPLICAR * | MAYOR O IGUAL >= | NOT | /= |
| MODULO % | DIFERENTE QUE != |  **= |
| DIVISION / | MENOR QUE < | | %= |
| POTENCIA ** | MENOR O IGUAL <= | | *= |

---

## :book: Operadores relacionales

### Operador de igualdad : ==

```Python
c = "Raul" == "raul"
print(c) # False por ser case sensitive
```

### Operador Diferente que : !=
```Python
a = 10 != 20
print(a) # True porque no son iguales
```

### Operador menor que: <
```Python
caso1 = 5 < 4
print(caso1) # falso proque 5 no es menor que 4
```

### Operador mayor que : >
```Python
caso2 = 5 > 3
print(caso2) # True porque 5 es mayor a 3
```

### Operador menor o igual que: <=
```Python
caso3 = 20 <= 10
print(caso3) # False porque 20 no es menor ni igual a 10
```


### Operador mayor o igual que: >=
```Python
caso4 = 20 >=10
print(caso4) # True porque 20 es mayor a 10
```

--

## :book: Operador logico

### NOT

Niega todo

```Python
print(not True) # False
print(not False) # True
```

## AND

Para ser verdadero AMBOS deben ser verdaderos

```Python
print(True and False) # False
print(True and True) # True
```

## OR
Con tener al menos un True -> es True

```Python
print(True or False) # True
palabra = "Python"
#len(palabra) me da la longitud, la cantidad de caracteres que tengo
# con palabra[0] accedo al primer caracter
print(len(palabra)<8 or palabra[0] == "f") # True porque la longitud de palabra es menor a 8
```

---

## :book: Operadores de asignacion

### Suma

```Python
numero1 = 10
numero1 +=10
print(numero1) # 20
```

### Resta

```Python
numero2 = 10
numero2 -=10
print(numero2) # 0
```
### Modulo

```Python
numero3 = 20
numero3 %= 2
print(numero3) # 0
```

### Division

```Python
numero4 = 30
numero4 /=5
print(numero4) # 6
```

### Potenciacion

```Python
numero5 = 2
numero5 **=3
print(numero5) # 8
```

---

## Tarea

- 1- Escriba un programa que lea dos numeros por teclado y determine con un valor booleano de True o False estos ejemplos:

Si los dos numeros son iguales

Si los dos numeros son diferentes

Si el primero es mayor que el segundo

Si el segundo es mayor o igual que el primero

```Python
primer_numero_ingresado = int(input("ingrese un primer numero entero: "))
segundo_numero_ingresado = int(input("Ingrese un segundo numero entero: "))
resultado1 = primer_numero_ingresado == segundo_numero_ingresado
print("Los dos numeros ingresados son iguales -> " , resultado1 )
# Si los dos numeros son diferentes
resultado2 = primer_numero_ingresado != segundo_numero_ingresado
print("Los dos numeros ingresados son diferentes -> " , resultado2)
# Si el primero es mayor que el segundo
resultado3 = primer_numero_ingresado > segundo_numero_ingresado
print("El primero es mayor que el segundo -> " , resultado3)
# Si el segundo es mayor o igual que el primero
resultado4 = segundo_numero_ingresado >= primer_numero_ingresado # tambien se puede poner como primer_numero_ingresado < segundo_numero_ingresado
print("El segundo es mayor o igual que el primero -> " , resultado4)
```

- 2- Conociendo los operadores logicos, realice una comprobacion si una cadena de texto ingresada desde teclado por el usuario tiene la longitud mayor o igual que 4 y a su vez que 7 (determinar con un valor booleano True o False)

```Python
cadena_ingresada = input("Ingrese una palabra: ")
longitud_palabra_ingresada= len(cadena_ingresada)
resultado5 = longitud_palabra_ingresada >= 4 and longitud_palabra_ingresada 
print("La cadena ingresada tiene la longitud mayor o igual que 4 y a su vez que 7 -> ", resultado5)
```


---
---

# :star: Dia 3

Temas:

- control de flujo y condicionales: sentencia if / bucle while / bucle for

---

## Control de flujo

Los script en Python es una instruccion que va de arriba hacia abajo y de izquierda a derecha.

Para alterar el flujo natural del programa tenemos las **condicionales**.

- Es importantísima la **identación** en Python, sino no funciona el loop. También es muy importante poner los **dos puntos**.

### :book: IF

```Python
edad = 20
if edad >=18:
  print("Es mayor de edad")
```

Solo si la condición dentro del **if** es True ( se cumple), se entra dentro del bucle, si no cumple (si es False) entonces nunca entrará.

### :book: IF ELSE

Si no cumple con la condición, va a entrar al else

```Python
edadAEvaluar = 7
if edadAEvaluar >=18:
  print("Es mayor de edad")
else:
  print("Eres menor de edad")
```

### :book: IF ELIF ELSE

Para evaluar más de dos condiciones.

```Python
edadActual = int (input("Escribe tu edad: "))
if edadActual >= 10 and edadActual <65:
  print('Eres Adulto')
elif edadActual >= 65:
  print('Eres adulto mayor')
else:
  print('Aun no eras adulto')
```

---

## Bucles

- Nos permiten repetir una porción de código tantas veces como queramos o necesitemos.

### :book: BUCLE WHILE

Si **edad2** no estuviera cambiando en cada iteracion -> estaría en un bucle infinito

Es muy importante que la variable vaya cambiando de valor y en algún momento la condición pasa de True a False, para cortar el loop

-> En el bucle WHILE siempre PRIMERO SE EVALUA LA CONDICION, o sea que si ya desde el inicio no se cumple, entonces nunca entra al bucle


```Python
edad2 = 1
while edad2 <=18:
  print("Es menor de edad")
  edad2+=1
```

Otro ejemplo

```Python
lenguajes = ['Python', 'Java', 'C', 'JavaScript', 'Go']
lenguajeSeleccionado = 0
while lenguajeSeleccionado < len(lenguajes):
  print(lenguajes[lenguajeSeleccionado])
  lenguajeSeleccionado+=1
```

### :book: BUCLE FOR

Es más potente para las **colecciones**, para poder iterar sobre listas, diccionarios, etc.

La variable **i**, va a ser la variable iteradora, va a ir recorriendo todos los elementos, uno por uno, es decir que en cada iteración se va modificando
Automaticamente Python la inicializa en 0 y la va incrementando de 1 en 1, es como el **forEach** de Java y de JavaScript

```Python
frutas = ['manzana', 'banana', 'uva', 'naranja']
for i in frutas:
  print(i)
```

Ejemplo de FOR IN RANGE:
```Python
for i in range(1,10):
  print(i)
```

-> crea una lista del 1 al 10, incluido, el segundo parámetro dentro de range() no se incluye, por eso no se ve el 11.  

---

## Tarea

- 1  Escriba un programa que almacene la cadena de caracteres contraseña en una variable, para luego preguntarle al usuario por la contraseña. Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con la guardada en variable.

```Python
contraseniaGuardada = "123456"
contraseniaIngresada = (input("Ingrese la contraseña : "))
if contraseniaIngresada == contraseniaGuardada:
  print("Contraseña ingresada correctamente")
else:
  print("Error al ingresar la contraseña")
```

- 2  Realice un programa que le pida al usuario dos números y muestre por consola su división. Si el divisor es cero el programa debe mostrar un error.

```Python
primerNumeroIngresado = int (input("Ingrese un numero: "))
segudoNumeroIngresado = int (input("Ingrese un segundo numero: "))
if segudoNumeroIngresado != 0:
   print(f"La division entre {primerNumeroIngresado} y {segudoNumeroIngresado} es : {primerNumeroIngresado/segudoNumeroIngresado}")
else:
  print("Error")
```

- 3 Escriba un programa que le pida al usuario por teclado un numero entero y muestre en consola si es par o impar.

```Python
esParOImpar = int (input("Ingrese un numero: "))
if esParOImpar / 2 == 0:
  print("Ingreso un numero PAR")
else:
  print("Ingreso un numero IMPAR")
```

- 4 Escriba un programa donde se evalué el ingreso a menores de edad, si la persona tiene menos de 19 años el programa le debe mostrar en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!

```Python
edadParaIngresar = int(input("Ingrese su edad para informarle si puede ingresar: "))
if edadParaIngresar >= 19:
  print("Bienvenido")
else:
  print("No puede ingresar")
```

--- 
---

# :star: Dia 4

Temas: Colecciones:

- Listas

- Tuplas

- Diccionarios

- Colas y Pilas

---

## Colecciones

-> Una coleccion permite agrupar varios objetos mediante un mismo nombre.

-> Puede guardar distintos tipos de elementos

-> Puede tener elementos repetidos

En Python tenemso distintos tipos de colecicones, como: listas, tuplas, diccionarios, colas y pilas.

---

## :book: Listas

-> Las listas agrupan elementos.

-> Van entre **corchetes**

-> Sus elementos se separan por **coma**

Así ya tengo mi lista declarada, por más que todavía no tenga elementos.

```Python
personas = []
```

Le asigno elementos
```Python
personas = ['Martin', 'Maria', 'Gonzalo', 'Raul','Pamela']
```

- Sus elementos se separan con **coma**

- Si quiero acceder a uno de los elementos, hay que recordar que los **indices** comienzan desdde **0**. Siempre el indice va a ser un numero menos que el total de los elementos

```Python
print(personas[0]) # Martin -> accedo al indice 0, es decir el primer elemento
print(personas[3]) # Raul -> accedo al indice 3, es decir el 4to elemento
print(personas[-1]) # accedo al ultimo elemento
print(personas[-2]) # accedo al anteultimo elemento
```

- Si quiero **eliminar** un elemento utilizo **del**

```Python
del personas[1] # con del elimino un elemento
print(personas) # se elimino el elemento con indicde ['Martin',  -> 'Gonzalo', 'Raul', 'Pamela']
```

- Si quiero **agregar** elementos, utilizo el metodo **.inser(indice, elemento)**, voy a tener dos parametros: **indice** con un numero voy a indicar en que indice lo agrego y con **elemento** voy a aclarar qué elemento voy a ingresar.
```Python
personas.insert( 0, 'Martina') # con .insert() agrego un elemento
print(personas)  # ['Martina', 'Martin', 'Gonzalo', 'Raul', 'Pamela'] asi agrego a Martina como primer elemento y desplazo todos un lugar
```

- Si quiero **agregar un elemento al final**, entonces utulizo el metodo **.append(elemento)**, aca solo tengo un argumento, ya que el indice no lo necesito porque siempre se agrega al final

```Python
personas.append('Mateo')  
print(personas) # ['Martina', 'Martin', 'Gonzalo', 'Raul', 'Pamela', 'Mateo']
```

- Las lista agrupan elementos, pueden ser elementos de distinto tipo, en una misma lista puedo tener String con Integer, por ejemplo.

```Python
listaMezclada = ['Martin', 10, True, ['Pyhton', 'Java', 'JavaScript'], 1.0]
print(listaMezclada) # ['Martin', 10, True, ['Pyhton', 'Java', 'JavaScript'], 1.0]
```

Si quiero acceder a Python que es una lista dentro de la lista
```Python
print(listaMezclada[3][0]) #Python
# me va a ignorar los elementos de indice 0 y 1, va a comenzar desde el elemento de indice 2 ->
print(listaMezclada[2:]) # [True, ['Pyhton', 'Java', 'JavaScript'], 1.0]
```

---

##  :book: Tuplas

-> A diferencias de las listas las tuplas son **inmutables** (como los vectores en  Java), sus elementos no varian, en este caso hay que crear la tupla y ya asignarle los elementos

-> van entre **parentesis** y sus elementos se separan con **coma**

-> Pueden tener distintos tipos de elementos.

```Python
tupla = (11, 'Python', True, [1,2,3])
print(tupla) # (11, 'Python', True, [1, 2, 3])
```

- Puedo acceder a sus elementos mediante los indices

```Python
print(tupla[0]) # 11
print(tupla[1:]) # ('Python', True, [1, 2, 3])
print(tupla[3][2]) # 3 -> asi veo la longitud de la lista dentro de la tupla, cuantos elementos tiene
```

-> Para **saber en que indice se encuentra determinado elemento** se utiliza el metodo **.index(elemento_a_buscar), hay que recordar que Python es case sensitive, prestar atencion a las mayusculas y las minusculas.

```Python
print(tupla.index(True)) # 2
```

-> Como la tupla puede tener elementos repetidos, **si quiero saber cuantas veces se encuentra un elemento**, utilizo el método **.count(elemento_a_buscar)**

```Python
print(tupla.count(11)) # 1
```

-> También funciona le método **len()** para saber la cantidad de elementos de una tupla

```Python
print(len(tupla)) # 5
print(len(tupla[4]))  # 3
```

-> No se puede utilizar el metodo append(), ya que la tupla **es inmutable**, por lo cual no se puede agregar nada a una tupla


---

## :book: Diccionarios

-> Son **colecciones no ordenadas**, siempre se conforman de pares **key**-**value**, aca la posicion ya no tiene importancia.

-> Para los diciconarios usamos **llaves**, para separar los elementos usamos la **coma**, y denominamos**clave : valor** (es decir que los dos puntos separan la key del value)

-> Son flexibles, se le pueden agregar o sacar paras de key-value

```Python
personas = {'Brian': 26, 'Maria': 22, 'Martin': 66, 'Patricia': 55}
print(personas) # {'Brian': 26, 'Maria': 22, 'Martin': 66, 'Patricia': 55}
```

-> Para ver el **value**, debo poner entre **corchetes** la **key**

```Python
print(personas['Brian']) # 26
print(personas['Maria']) # 22
```

-> Si queresmos **agregar un nuevo par key-value**

```Python
personas['Jose'] = 42  # para agregar un nuevo par key-value, se agrega ala final
print(personas) # {'Brian': 26, 'Maria': 22, 'Martin': 66, 'Patricia': 55, 'Jose': 42}
```

-> Si queremos **modificar** un **value**

```Python
personas['Brian'] = 23
print(personas['Brian'])  # 23, asi modifico un value
```

-> Para **eliminar** un par **key-value** utilizamos el metodo **del**

```Python
del personas['Martin'] # asi elimino el par key-value que tiene como key Martin
print(personas) # {'Brian': 23, 'Maria': 22, 'Patricia': 55, 'Jose': 42}
```


---

##  :book: Colas y Pilas


Voy a simular una fila del supermercado, hay 4 personas que hacen al cola, el primero es Jose

```Python
fila = ['Jose', 'Maria', 'Raul', 'Paola'] 
print(fila) # ['Jose', 'Maria', 'Raul', 'Paola']
```

-> Para **agregar** utilizo el metodo **.append()**

```Python
fila.append('Romina')  # agrego un elemento al final -> ['Jose', 'Maria', 'Raul', 'Paola', 'Romina']
```

-> El primero que ingreso debe ser el primero en salir

```Python
i = fila.pop(0) # elimina al ultimo de la fila si entre los parentesis no aclaro nada, pero la ponerle el 0 me elimina el primero
print(i) # Jose
print(f'Estan atendiendo a {i}')  # Estan atendiendo a Jose, con el format puedo concatenar un String con una varaible, es como el template literal de JS pero en este caso la variable va sin el $
print(fila) #  ['Maria', 'Raul', 'Paola', 'Romina']
```


---

## :book: Conjuntos

-> Es una coleccion no ordenada, no tiene elementos repetidos, **sus elementos son unicos**

-> Un conjunto lo declaro con **set()**:

```Python
conjunto = set() # asi declaro al conjunto
```

-> En el conjunto también utilizo **llaves**, y como antes utilice **set()**, entonces Python entinedo que es un conjunto y no un diccionario (ya que los diccionarios también van entre llaves)

```Python
conjunto = {2, 'Python', 2, 'Euge', False}
print(conjunto) # {False, 'Python', 2, 'Euge'} como el 2 esta repetido me muestra solo uno, pero al no ser ordenado no se cual de los dos me muestra
```

-> No puede tener una coleccion(lista, tupla, diccionario), como elemento.

-> Se pueden **agregar** elementos con **.add()**

```Python
conjunto.add('Martin') # agrega un elemento en un lugar aleatorio ya que el conjunto no es una coleccion ordenada
print(conjunto) # {False, 2, 'Martin', 'Python', 'Euge'}
```

-> Si quiero **eliminar** un elemento utilizo el metodo **.discard(elemento_a_eliminar)**

```Python
conjunto.discard('Euge')
print(conjunto) # {False, 2, 'Martin', 'Python'}
```

-> Para **eliminar todos los elementos juntos** utilizo el metodo **.clear()**

```Python
conjunto.clear() # para eliminar todos los elementos
print(conjunto)  # set()
```

-> Para **saber si un elmemento esta en el conjunto** utilizo el metodo **elemento in conjuno**, va a dar un valor boolean, True si se encuentra y False si no se encuentra.

```Python
print('Python' in conjunto)  # True asi veo si un elemento esta en el conjunto
# TAMBIEN LO PUEDO NEGAR CON NOT
print('Marcos' not in conjunto)  #  al negar de que esta me va a dar True, ya que Marcos no se encuentra
```

---

## Tarea

- 1 Escriba un programa que almacene en una Lista los cursos que has cursado o los que te gustaría cursar en Udemy. Luego muestre la lista por consola.

```Python
for i in listaDeCursos:
  print(i)
```

- 2 Escriba un programa que almacene personas en una lista, luego que le muestre por pantalla el mensaje de ‘Su nombre es ‘nombre’

```Python
listaDePersonas = ['Analia', 'Carlos', 'Agustin', 'Andres']
for i in listaDePersonas:
  print(f'Su nombre es {i}')
```

- 3 Escribir un programa que guarde en una variable un diccionario con los siguientes valores {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y muestre en consola el símbolo o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

```Python
diccionarioDeMonedas =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisaElegida = input("Ingrese una divisa -en palabra, con la primer letra en mayuscula-: ")
if divisaElegida.title() in diccionarioDeMonedas:
    print(f'El simbolo  es: {diccionarioDeMonedas[divisaElegida.title()]}')
else:
  print("La divisa no se encuentra en el diccionario")

```

- 4  En una tupla coloque los siguientes valores: números enteros, decimales, String, colecciones. Luego muestre en consola.

```Python
tupla = (20, 14.5, 'Hello', [1, 2, 3, 4, 5])
print(tupla)
```

-> La función **title()** en python es el método de cadena de Python que se utiliza para convertir el primer carácter de cada palabra en mayúsculas y los caracteres restantes en minúsculas en la cadena y devuelve una nueva cadena.
 

---
---

# :star: Dia 5

Tema: Funciones:

- Declarar funciones

- Retornar valores

- Enviar valores

- Argumentos indeterminados

- Argumento sy parametros

---

Ya vinimos utulizando algunas funciones, como por ejemplo: 

**print()**  -> imprime un argumento por pantalla

**len()** -> determina la longitud de un elemento

---

## :book: Declarar funciones

**def** es la palabra reservada para definir una funcion

Es muy importante la identación

```
def nombreFuncion():
 # aca va la funcion
```

Ejemplo en codigo:
```Python
def saludar(): # declaramos nuestra funcion
  print("Hola") #le damos cuerpo a la funcion
saludar() # invoco, llamo a la funcion
```

La funcion nos ayuda a reutilizar código, va a ser muy importante con los modulos

Otro ejemplo en codigo:

```Python
def sumar():
  i = 10
  m = 5
  print('El resultado de la suma es: ', i + m)  
```

Hay que tener en cuenta que las variables que declare dentro de la funcion, solo existiran dentro de la funcion, tienen un ***scope local** y es el de la misma funcion, si por ejempplo:


```Python
i = 100
def sumar():
  i = 10
  m = 5
  print('El resultado de la suma es: ', i + m)  
sumar() # invoco a la funcion sumar -> El resultado de la suma es:  15 , el 100 es un valor global de i, no es para el scope de la funcion
print(i)  # 100 es la variable global, porque esta fuera de la funcion
```


Otro ejemplo:

```Python
def restar():
  i = 80
  m = 20
  print('El resultado de tu resta es: ', + i-m)
restar() # invoco a la funcion restar -> El resultado de tu resta es:  60
```

-> si presto atencion tanto en suma() como en resta() utilice las variables i y m, pero como solo tiene alcance local, no existen fuera e la funcion, no hya inconveniente

---

## :book: Retornar valores

```Python
def saludar():
  return "Buenos dias"
```

```Python
saludar()
```
Por consola no se ve nada, lo que hace la funcion es retornarme el string "Buenos dias"

```Python
print(saludar()) # veo por consola: Buenos dias
```

Otro ejemplo, si en el return ya tengo el print() loego solo invoco a la funcion y veo el mensaje:

```Python
def saludoConReturn():
  return print("Buenos dias desde el return")

saludoConReturn()  # Buenos dias desde el return
```

Puedo retornar String, int, diccionario, tupla, etc; todo tipo de elementos
---

## :book: Enviar valores

```Python
def sumar(op1, op2): #op1 y op2 son argumentos
  resultado = op1+op2
  return resultado

print(sumar(2,3))  # 10
```

Al llamar/invocar a la funcion debo incluir la misma cantidad de argumentos que tiene la funcion.

Otro ejemplo:

```Python
def saludar(nombre):
  return print(f"Hola {nombre}")
saludar("Euge")  # Hola Euge
```

---

## :book: Argumentos indeterminados

```Python
def sumar(*args):
  print(args)

sumar(10,20,30,40,50,60,70)  # (10, 20, 30, 40, 50, 60, 70)
```

```*args``` indica que son varios argumentos, pero no se exactamente cuantos, pueden ser numeros(int), string, lista, etc el tipo de argumento.


Otro ejemplo:

```Python
def mostrar(*args):
  for i in args:
    print(i)

mostrar('Python', True, 10, 2.8, [1, 2, 3])
```

Y por consola veo:

```
Python
True
10
2.8
[1, 2, 3]
```

---

## :book: Tarea

- 1 - Escriba una función que muestre por consola un saludo personalizado. Por ejemplo ‘¡Hola mundo!’

```Python
def holaMundo():
  return print("Hola mundo!")
holaMundo()
```
- 2 -  Escriba una función que reciba un nombre por parámetro y que luego muestre en pantalla ```¡Hola <nombre>!```

```Python
def saludoPersonalizado(nombre):
  return print(f"Hola {nombre}")
saludoPersonalizado("Ana")
```

- 3 -  Cree una función que le pida el usuario su nombre y su edad, luego muestre en pantalla los resultados.

```Python
def mostrar():
  nombre = input("Ingrese su nombre: ")
  edad = input("ingrese su edad: ")
  return print(f"Ingreso : {nombre} , {edad}")
mostrar()
```

- 4 - Definir una función que reciba dos números por parámetros y que luego los sume.

```Python
def suma(numero1, numero2):
  resultado = numero1 + numero2
  return print(f"la suma de {numero1} y {numero2} es: {resultado}")
suma(2,8)
```

---
---

# :star: Dia 6 : Manejo de errores

Un claro error es la division por cero, en este caso Python muestra el error y se me bloquea el programa, todo lo que sigue a continuación no se ejecuta.

Para eso vamos a tener que aplicar excepciones, asi saltea la linea de codigo y continua con el flujo de ejecucion.

---

## :book: Errores y Excepciones

```Python
def multiplicar(num1, num2):
  try:
    return num1 * num2
  except ZeroDivisionError:
    print("ERROR. No se puede dividir por 0")
    return "Operacion no valida"
```


Otro ejemplo, donde el error lo guardo en la variable **c** que la uso como alias, para no escribir todo el nombre del error:

```Python
try:
  c = int(input("Ingrese un valor: "))
  c/0
except Exception as c:
  print(type(c).__name__)
```

---

## :book: Excepciones multiples

```Python
try:
  c = int(input("Ingrese un valor: "))
  c/0
except ValueError:
  print("Debe ingresar un numero, no puede dividir una cadena de caracteres con un numero")
except Exception as c:
  print(type(c).__name__)  # ZeroDivisionError
```

---

## :book: Tarea

- 1 - Encuentra el error en la siguiente línea de código. Luego tendrás que crear una excepción para evitar que el programa se caiga. Además, debes explicarle al usuario que fue lo que sucedió y darle la solución.

• valor = 10/0

```Python
def dividir():
  num1 = int(input("Ingrese un valor: "))
  num2 = int(input("Ingrese otro valor: "))
  try:
    return print(num1 / num2)
  except ZeroDivisionError:
    print("ERROR. No se puede dividir por 0")
    return "Operacion no valida"

dividir()
```

- 2 - Encuentra el error en la siguiente línea de código. Luego tendrás que crear una excepción para evitar que el programa se caiga. Además, debes explicarle al usuario que fue lo que sucedió y darle la solución.

• miLista = [1,2,3,4,5 ]

• miLista [7]


```Python
miLista = [1,2,3,4,5]

def imprimirElemento():
  try:
    indice = int(input("Ingresa un numero, para mostrar un elemento de esta lista: 1,2,3,4,5 : "))
    return print(miLista[indice])
  except IndexError:
    print("Error, numero fuera del limite, debe ser entre 0 y 4")

imprimirElemento()
```

---
---

# :star: Programacion Orientada a Objetos

Es un paradigma de programacion.

Algunos conceptos son:

- clase: mecanismo para definir un tipo de dato que continene atributos y metodos

- instancia: es de una clase

- variable de clase: comparte todas las instancias de una clase

- variable de instancia: contiene datos de los objetos y atributos asociados a la instancia actual de la clase

- metodo: son los procedimientos (las funciones), las acciones del objeto.

- objeto: estructura de datos, que contienen informacion(CARACTERISTICAS) en forma de ATRIBUTOS y codigo en forma de procedimiento(FUNCIONES) conocido como METODO.

Vemos un ejemplo:

Tengo una clase **Persona**, con sus atributos ( **nombre**, **apellido**, **profesion**, **edad**) y sus metodos (**obtener el nombre de la persona**, **cambiar el nombre de la persona**, etc).


---

## :book: Clases Gelatina

- el nombre de la clase siempre lleva la primer letra en mayuscula

Ejemplo de clase.

```Python
class Gelatina:
  # es mi constructor, el self es como el this
  def __init__(self, sabor, color, tamanio):
      self.sabor = sabor
      self.color = color
      self.tamanio = tamanio

  # un metodo de la clase
  def imprimir(self):
    print(f'La gelatina es de {self.sabor}')
    print(f'La gelatina se ve de de {self.color}')
    print(f'La gelatina es de un tamaño {self.tamanio}')
# instancio la clase Gelatina para crear mi primer objeto    
gelatina1 = Gelatina('Frutilla', 'Rojo', 'Grande')
gelatina1.imprimir()  # invoco al metodo para imprimir
```

---

## :book: Clase Persona

```Python
class Persona:
  def __init__(self, nombre, edad, sexo):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo

  def datosPersonales(self):
    print(f'El nombre de la persona es: {self.nombre}')
    print(f'La edad de la persona es: {self.edad}')
    print(f'El sexo de la persona es: {self.sexo}')

persona1 = Persona('Eugenia', 25, 'Femenino')
persona1.datosPersonales()
```

---

## :book: Metodos especiales

**del** y **str** (este es como el .toString de Java)

```Python
class Coche:
  def __init__(self, marca, kilometros, anio):
    self.marca = marca
    self.kilometros = kilometros
    self.anio = anio
    print(f'Se ha crado un auto {self.marca}, con {self.kilometros} kilometros')

  def arrancar(self, arrancamos):
    self.enmarcha = arrancamos
    if(self.enmarcha):
      return "El auto esta encendido"
    else:
      return "El auto este apagado"

  def __del__(self): # con este metodo elimino el objeto coche
    print(f'Se ha vendido el auto {self.marca}')

  def __str__(self):
  return 'El auto es un {}, tiene {} kilometros, y es del año {}'.format(self.marca, self.kilometros, self.anio)
# instancio un objeto
miCoche = Coche('Audi', 200, 1995)
print(str(miCoche))
print(miCoche.arrancar(True)) # El auto esta encendido
del(miCoche) # Se ha vendido el auto Audi
```


---

## :book: Encapsulamiento

Forma de modificar un atributo:

```Python
miCoche2 = Coche('Audi', 222, 1990)
miCoche2.marca= 'Peugeot' # asi modifico un atributo del objeto
print(str(miCoche2)) # El auto es un Peugeot, tiene 222 kilometros, y es del año 1990
```

Lo cual no esta bueno que cualquier puede meterse desde afuera y modifique mi atributo, por eso el encapsulamiento, para solo poder modificar un atributo desde dentro de mi clase.

Para **encapsular** utilizo el doble guion bajo :

```Python
class Coche:
  def __init__(self, marca, kilometros, anio):
    self.__marca = marca  # con el doble guion bajo encapsulo el atributo marca, lo hago privado
    self.kilometros = kilometros
    self.anio = anio
    print(f'Se ha crado un auto {self.__marca}, con {self.kilometros} kilometros')

  def __str__(self):
    return 'El auto es un {}, tiene {} kilometros, y es del año {}'.format(self.__marca, self.kilometros, self.anio) 

miCoche1 = Coche('Audi', 222, 1992)
miCoche1.marca = 'Peogeot' # al estar encapsulado no puedo cambiar el atributo
print(str(miCoche1)) # me muestra Audi
```

---

## :book: Tarea

- 1 -Cree una clase Persona con sus atributos correspondientes: nombre, edad, sexo, nacionalidad. Luego cree una instancia de la clase Persona.

```Python
class Persona:
  def __init__(self, nombre, edad, sexo, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.nacionalidad = nacionalidad
  
  def __str__(self):
    return f'La persona se llama {self.nombre}, tiene {self.edad} años, es de sexo {self.sexo} y es de nacionalidad {self.nacionalidad}'
persona1 = Persona('Eugenia', 37, 'Femenino', 'Argentina')
print(str(persona1))
```

- 2- Cree una clase Auto con sus atributos correspondientes: marca, modelo, año, color. Defina también un método, donde luego al instanciar la clase nos diga si el auto esta encendido o apagado.

```Python
class Auto:
  def __init__(self, marca, modelo, anio, color):
    self.marca = marca
    self.modelo = modelo
    self.anio = anio
    self.color = color
  
  def encender(self, encendemos):
    self.encendido = encendemos
    if(self.encendido):
      return "El auto esta encendido"
    else:
      return "El auto este apagado"

miAuto = Auto('Fiat', 'Uno', 2020, 'Azul')
print(miAuto.encender(True))
```

---
---

# :book: Herencia

---
## :star: Herencia

Permite reutilizar código.

Utilizamos las clases.

Voy a tener la clase **Persona** y la clase **Empleado**, esta ultima va a heredar de la clase Persona, es como un 'hijo' de la clase Padre, entonces va a tner las mismas caracteristicas(propiedades) que Persona más las propias. Y de este modo nos ahorramos de repetir el codigo de las propiedades. También hereda los métodos.


Ejemplo en codigo:

```Python
class Empleado(Persona):

  def datosEmpleado(self, vacaciones, salario):
    print(f'Sus dias de vacaciones son: {vacaciones}')
    print(f'Su salario es: {salario}')
```

Tengo a mi clase Empleado que EXTIENDE de la calse Persona, va a tener todos los atributos y metodos de la clase Persona, más los propios.


### Un ejemplo con una clase y la clase hija con constructores en cada una

Tengo la clase Persona:

```Python
class Persona(object): #Clase que representa una Persona
  def __init__(self, cedula, nombre, apellido, sexo): # Constructor de clase Persona
      self.cedula = cedula
      self.nombre = nombre
      self.apellido = apellido
      self.sexo = sexo

  def __str__(self): # Devuelve una cadena representativa de Persona
      return "%s: %s, %s %s, %s." % (
          self.__doc__[25:34], str(self.cedula), self.nombre, 
          self.apellido, self.getGenero(self.sexo))

  def hablar(self, mensaje): # Mostrar mensaje de saludo de Persona
      return mensaje

  def getGenero(self, sexo): # Mostrar el genero de la Persona
    genero = ('Masculino','Femenino')
    if sexo == "M":
        return genero[0]
    elif sexo == "F":
        return genero[1]
    else:
        return "Desconocido"
```

La clase Persona tiene los métodos ```__init__```, ```__str__```, ```hablar``` y ``` getGenero```. Sus atributos son ```cedula```, ```nombre```, ```apellido``` y ```sexo```.

La instancia de dos nuevos objetos Persona seria de la siguiente forma:

```Python
persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
persona2 = Persona("V-23569874", "Ana", "Poleo", "F")
```


Y la clase hija Supervisor

```Python
class Supervisor(Persona): # Clase que representa a un Supervisor

  def __init__(self, cedula, nombre, apellido, sexo, rol): # Constructor de clase Supervisor
    Persona.__init__(self, cedula, nombre, apellido, sexo) # Invoca al constructor de clase Persona
    self.rol = rol  # Nuevos atributos
    self.tareas = ['10','11','12','13']  # Nuevos atributos

  def __str__(self): # Devuelve una cadena representativa al Supervisor
    return "%s: %s %s, rol: '%s', sus tareas: %s." % (
      self.__doc__[26:37], self.nombre, self.apellido, 
      self.rol, self.consulta_tareas())

  def consulta_tareas(self): # Mostrar las tareas del Supervisor
    return ', '.join(self.tareas)
```

Para instanciar un objeto de la clase Supervisor
```Python
supervisor1 = Supervisor("V-16987456", "Jen", "Paz", "D", "Chivo")
print "\n" + str(supervisor1) + "\n"
# Como la instancia de objeto supervisor1 hereda los atributo(s) y método(s) de la clase Persona usted puede reusarlo y llamarlo de la siguiente forma:
print "- Cedula de identidad: {0}.".format(supervisor1.cedula)
print "- Nombre completo: {0} {1}.".format(
	supervisor1.nombre, supervisor1.apellido)
print "- Genero: {0}.".format(
	supervisor1.getGenero(supervisor1.sexo))
print "- {0} {1} dijo: {2}".format(
	supervisor1.nombre, supervisor1.apellido, 
	supervisor1.hablar("A trabajar Leonardo!!!".upper()))
# Si desea usar los atributo(s) y método(s) heredados de la clase Supervisor se puede imprimir de la siguiente forma:
print "- Rol: {0}.".format(supervisor1.rol)
print "- N. Tareas: {0}.".format(supervisor1.consulta_tareas())
```

---

## :star: Herencia Multiple

A diferencia de lenguajes como Java y C#, el lenguaje Python permite la **herencia múltiple**, es decir, se puede heredar de múltiples clases.

La herencia múltiple es la capacidad de una subclase de heredar de múltiples súper clases.

Esto conlleva un problema, y es que si varias súper clases tienen los mismos atributos o métodos, la subclase sólo podrá heredar de una de ellas.

En estos casos Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase:

```Python
class Destreza(object): # Clase la cual representa la Destreza de la Persona
  def __init__(self, area, herramienta, experiencia): # Constructor de clase Destreza
    self.area = area
    self.herramienta = herramienta
    self.experiencia = experiencia

  def __str__(self): # Devuelve una cadena representativa de la Destreza
    return """Destreza en el área %s con la herramienta %s, 
    tiene %s años de experiencia.""" % (
        str(self.area), self.experiencia, self.herramienta)

class JefeCuadrilla(Supervisor, Destreza): # Clase la cual representa al Jefe de Cuadrilla
  def __init__(self, cedula, nombre, apellido, sexo, 
    rol, area, herramienta, experiencia, cuadrilla): # Constructor de clase Jefe de Cuadrilla
    # Invoca al constructor de clase Supervisor
    Supervisor.__init__(self, cedula, nombre, apellido, sexo, rol)
    # Invoca al constructor de clase Destreza
    Destreza.__init__(self, area, herramienta, experiencia)
    self.cuadrilla = cuadrilla # Nuevos atributos

  def __str__(self): # Devuelve cadena representativa al Jefe de Cuadrilla
    jq = "{0}: {1} {2}, rol '{3}', tareas {4}, cuadrilla: {5}"
    return jq.format(
        self.__doc__[28:46], self.nombre, self.apellido, 
```

#### Method Resolution Order (MRO)

Ese es el orden en el cual el método debe heredar en la presencia de herencia múltiple. Usted puede ver el MRO usando el atributo ```__mro__```.

```Python
JefeCuadrilla.__mro__
```

```
(<class '__main__.JefeCuadrilla'>,
<class '__main__.Supervisor'>,
<class '__main__.Persona'>,
<class '__main__.Destreza'>,
<type 'object'>)
```


```Python
Supervisor.__mro__
```

```
(<class '__main__.Supervisor'>,
<class '__main__.Persona'>,
<type 'object'>)
```

```Python
Destreza.__mro__
```

```
(<class '__main__.Destreza'>,
<type 'object'>)
```
---

## :star: Tarea

- 1 - Realice una clase persona con sus atributos correspondientes, luego haga una clase empleado que herede los atributos de la clase Persona. Por último, cree un método de la clase empleado e instancie la clase.

```Python
class Persona():
  def __init__(self, nombre, apellido, edad, nacionalidad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.nacionalidad = nacionalidad

class Empleado(Persona):
  def __init__(self, nombre, apellido, edad, nacionalidad, estado):
    Persona.__init__(self, nombre, apellido, edad, nacionalidad)
    self.estado = estado

  def estaJubilado(estado):
    if (estado == True):
      print('Esta jubilado')
    else:
      print('Es un empeado activo, no se jubilo todavia')

empleado1 = Empleado('Ana', 'Gonzalez', 35, 'Peruana', True)
empleado1.estaJubilado()
```

---
---

# :book: Dia 9

## :star: Cadenas (String)

Algunos métodos, son:

```Python
nombreIngresado = input('ingrese su nombre por favor: ')
print('El nombre del usuario es: ', nombreIngresado)
```

**.upper()** ->  Metodo para pasar todo en mayuscula
```Python
print ('El nombre todo en mayuscula es: ', nombreIngresado.upper())
```

**.lower()** ->  Metodo para pasar todo en minuscula
```Python
print ('El nombre todo en minuscula es: ', nombreIngresado.lower())
```

**.capitalize()** ->  Si necesito la primer letra en mayuscula y el resto en minucula
```Python
print ('El nombre capitalizado es: ', nombreIngresado.capitalize())
```

**.isdigit()** -> corroboro si ingrese un int
```Python
mensaje = 'Hola mundo'
print(mensaje.isdigit()) # False, corrobora que no tengo un valor numerico
mensaje = '123'
print(mensaje.isdigit()) # True
numeroEntero = 123
#print(numeroEntero.isdigit()) # AttributeError: 'int' object has no attribute 'isdigit'
```

**.split()** -> para separar
```
segundoMensaje= 'Hola me llamo Eugenia'
print(segundoMensaje.split('-')) # ['Hola me llamo Eugenia']
print(segundoMensaje.split(' ')) # ['Hola', 'me', 'llamo', 'Eugenia']
```

**.isalnum()** -> busca si es alfanumerico

Si llego a poner ```'abc123 '``` no me da que es alfanumerico por el espacio.

```Python
print(segundoMensaje.isalnum()) # False busca si es alfanumerico
```

## :star: Arrays (lista)


Algunos metodos de los arrays, son :

**.append()** -> agrego el elemento al final de la lista
```Python
lista = [1, 2, 3, 4, 5]
lista.append(6) # agrego al final
print(lista) # [1, 2, 3, 4, 5, 6]
```

**.extend()** -> para unir listas
```Python
lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9]
lista.extend(lista2) # para unir listas
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


**.count(arg)** -> para ver cuantas veces tengo dicho argumento en la lista

```Python
print(lista.count(1)) # 1
```

**index(arg)** -> para ver en que indice esta un elemento que paso como argumento
```Python
print(lista.index(1)) # 0 
```

**.insert()** -> Tengo dos argumentos, el primero es en el indice en que voy a agregar el elemento, el segundo es el elemento a agregar.

```Python
lista.insert(2,0) # voy a agregar en el indice 2 al numero 0
print(lista) # [1, 2, 0, 3, 4, 5, 6, 7, 8, 9]
```

**.len()** -> para saber la longitud, la cantidad de elementos
```Python
print(len(lista)) # 10
```

**.pop()** -> borra el ultimo elemento
```Python
print(lista.pop()) # 9
```

**.remove(arg)** -> se pasa como argumento lo que se quiere eliminar
```Python
lista.remove(0) # voy a eliminar el 0
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8]
```

**.reverse()** ->  me la da vuelta el ultimo elemento pasa a ser el primero,el anteultimo elemento pasa a ser el segundo y asi.
```Python
lista.reverse()
print(lista) # [8, 7, 6, 5, 4, 3, 2, 1]
```

**.sort()** -> ordena de menor a mayor
```Python
lista.sort() # los ordena de menor a mayor
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8]
```

## :star: Diccionarios

Algunos de los metodos especiales de los diccionarios(van entre llaves, son de key-value), son:

teneindo este diccionario:

```Python
personas= {'Martin':'Martinez', 'Jose':'Alvarez', 'Maria':'Gomez'}
```

**.get(key)** -> Si la key esta en el doccionario me da el valor
```Python
print(personas.get('Jose')) # alvarez
```

**.key()** -> me muestra las key en una lista
```Python
print(personas.keys()) # dict_keys(['Martin', 'Jose', 'Maria'])
```

**.values** -> me muestra los values en una lista
```Python
print(personas.values()) # dict_values(['Martinez', 'Alvarez', 'Gomez'])
```

**.items()** -> se genera una lista con key-value de cada item del diccionario
```Python
print(personas.items()) # dict_items([('Martin', 'Martinez'), ('Jose', 'Alvarez'), ('Maria', 'Gomez')])
```

```Python
```

Con un **FOR** recorro todo el diccionario y voy imprmiendo cada par **clave** **valor**
```Python
for clave, valor in personas.items():
  print(clave, valor)
"""
Martin Martinez
Jose Alvarez
Maria Gomez
"""
```

**.pop()** -> para eliminar la KEY con el valor indicado
```Python
personas.pop('Martin') 
print(personas) # no muestra a Martin, elimino tanto la clave como el valor
```

**.clear()** -> me elimina todos los elementos
```Python
personas.clear() 
```

## :star: Conjuntos

Algunos metodos de los conjuntos, son:

**.set()** -> indica que va a ser un **conjunto**

**.add()** -> para ir agregando elemento por elemento
```Python
conjunto = set()
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
print(conjunto) # {1, 2, 3}
```

**.discard()** -> para eliminar el elemento que indico entre ()
```Python
conjunto.discard(1)
print(conjunto) # { 2, 3}
```

**.copy()** -> hago una copia del conjunto
```Python
conjunto2 = conjunto.copy() 
print(conjunto2) # { 2, 3}
```

**.clear** -> elimina todos los elementos de los conjuntos
```Python
conjunto.clear() 
print(conjunto) # set()
```

---
---

# :book: Dia 10

## :star: Modulos

## :star: Paquetes

## :star: Ejercicios
```Python
```

```Python
```

```Python
```

## :star: Tarea

- 1 - Cree un modulo con todas las operaciones matemáticas, luego impórtela en un archivo.py y realice las operaciones matemáticas
llamando a cada función.

- 2 - Cree un modulo que obtenga una función que solamente diga ‘Hola mundo’ luego impórtelo en un archivo.py y muéstrelo por
consola.
