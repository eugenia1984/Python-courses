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
---