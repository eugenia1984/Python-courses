# :star: Python 3 Plus: python desde Cero + Data Analysis y Matplot (Numpi en Udemy)

---

¿Qué esperas? Te llevaremos de la mano en cada uno de los temas para que te conviertas en un experto de Python y del Data Analysis.

El objetivo de la primera sección del curso es que sin conocimientos previos aprendas con ejercicios prácticos a:

- Identificar los tipos de datos.

- Definir funciones.

- Crear clases y objetos con la POO.

- Herencia y multiherencia en las clases.

- Leer y manipular datos desde archivos de texto.

- Controlar el flujo del programa.

- Manejar errores y excepciones.


En la segunda sección del curso aprenderemos:

- Como crear una Base de Datos con Python para leer y escribir datos en ella.

- A usar Numpy para trabajar con arrays y para generar muestras aleatorias.

- A importar datos desde un CSV o desde un Excel para analizarlos.

- A trabajar con fechas y variables de diferentes formatos.

- A exportar los datos tratados a Excel.

- A generar representaciones gráficas de la información para tener un mejor entendimiento de ella.

- Tambien abordamos varios ejercicios donde ponemos en practica lo aprendido durante las lecciones.

---

## Lo que aprenderás

- Aprenderás a programar en Python 3 desde cero.

- Aprenderás a instalar los programas necesarios para codificar en Python 3.

- Sabras utilizar todos los Tipos de Datos que hay en Python 3.

- Crearás código utilizando todas las Estructuras de Control de Python 3.

- Aprenderás a definir funciones.

- Aprenderás a extraer y manipular información desde archivos de texto.

- Aprenderás Programación Orientada a Objetos de una manera sencilla y amigable.

- Análisis de datos con Python

- Aprenderás a analizar grandes volúmenes de datos rápidamente con Pandas.

- Aprenderás a encontrar relaciones entre las variables de tus datos.

- Aprenderás como hacer gráficas atractivas para los datos.

- Aprenderás a generar representaciones gráficas de la información para tener un mejor entendimiento de ella.

- Aprenderás a exportar los datos tratados a Excel.

- Aprenderás a importar datos desde un CSV o desde un Excel para analizarlos.

- Aprenderás como crear una Base de Datos con Python para leer y escribir datos en ella.

---
---

# : book: Introduccion

## ¿ Qué es Python ?

- Popular lenguaje de programación **open source**

- Python es **multi-paradigma** (programacion funcinal, imperativa, orientada a objetos)

- Lenguaje con **tipado dinamico** (no se debe definir un tipo de dato para la variable al declararla, sino que se le asigna a partir del dato que alamacena, y puede ir modificando el tipo de dato almacenado). Cada variable hace referencia a un dato guardado en memoria.

- Enfocado a la **productividad**, a la calidad y claridad de código. Es un lenguaje accesible a las personas, es entendible, leguible, modificado.

- **Lenguaje de alto nivel** sencillo de programar, trabaja con un interprete, se trabaja fácilmente, no hay que compilar.

---

## Instalar Anaconda

Desde la web [anaconda.com](http://www.anaconda.com) la bajamos e instalamos, seleccionamos la segunda opción al final de todo y listo.

---

## Jupiter

Es la interrfaz donde vamos a escribir el codigo.

Desde el buscador de inicio, buscamos *jupyter* -> *jupyter anaconda notebook*

Y se nor abre en un browser: ```localhost:8888/tree```

Estan los botones


**New** -> **python 3** para abrir un nuevo archivo

**quit** para salir


---
---

# :book: Tipo de Objetos

## Variables


Como Python es un lenguaje de tipado dinamico, no necesita que se declaren los tipos de valores que almacenara una variable.

La variable es un espacio de memoria donde guardo una variable y le asigno un valor.

### ¿ Como las nombro ?

Con letras, puede contener caracteres alfanumericos

No admite espacios en blancos, utilizo camelCase o snake_case

Hay palabras reservadas que no se pueden usar, como: Python 3.x, False, continue, in, not, return, yield

El nombre de la variable es case sensitive (Python no es lo mismo que python).

### ¿ Cómo asigno valores ?

Con el **=**, por ejemplo:

**nombre_de_la_variable** **=** **valor_a_designar**
```Python
x=30
print(x)  # 30
nombre = "Maria Eugenia"
print(nombre)  # Maria Eugenia
```

En Python los **tipos primitivos** son :

- Numeros

- Cadenas de caracteres (String) -> siempre van entre comillas

- Booleans

- Tuplas

- listas

- diccionarios


---

## Metodos

Son funciones de clase, esto quiere decir que cada tipo de variable incluye unas funciones asociadas a ella desde su definición.

```Python
x.__add__(10)  # el metodo add , sumara lo que paso por parametro (10)
print(x) #40
```

Diciconario, coleccion de datos, con **key**:**value**.
```Python
diccionario = ['uno': x, 'dos':x.__add__(10)]
diccionario
# ['uno': 30, 'dos':40]
print(f'{nombre.title()} cuesta {diccionario['uno']} pesos y el otro libro {diccinario{'dos'}} pesos')
```

Utilizando **.dir()** se puede buscar el método disponible, entre () ponemos la variable de la cual queremos sabe rle metodo, por ejemplo ```Python dir(x)```

También está la función **help()** que nos muestra la ayuda, por ejemplo ```Python help(x)```

---

## :star: Number

Podemso asignarle valores a las varaibles.

Python tiene 4 tipos de varaibles para alamcenarlos

### INT (integer / entero)
```Python
x = 12+3
print(x) # 15
x = x.__add(5)
print(x) # 20
x = x -2
print(x) # 18
```

Siempre que almacenemos un numero entero será **int**

Se puede utilizar el método **.__add__(valor_a_sumar)**
### FLOAT (flotante / decimal)

Es un flotante, un decimal, el decimal en Python se marca con el **.**, no usamos la coma para separar el entero del decimal.

```Python
y = 4.5
print(y) # 4.5
```

### COMPLEX


Los números imaginarios

```Python
c = 1+2j
type(c)
parte_real = c.real
parte_imaginaria = c.imag
print(parte_real)
print(parte_imaginaria)
```


### Función type

Para saber el tipo de dato

```Python
y = 3.5
type(y) #float
```

## :star: String

Son secuencias de caracteres dentro de comillas, pueden ser comillas simples o dobles.

Con **print()** mostramos por pantalla el texto, y podemos editarlo con tabulaciones y saltos de linea.

Los String pueden ser almacenados en variables.

```Python
nombre = " Martina"
print(nombre) # Martina
print(type(nombre))  # <class 'str'>
```

```Python
print("una cadena  \tseparada por una tabulacion") # Para tabular, dejar un espacio
print("una linea  \notra linea") # para un salto de linea
print(r"hola/mundo") # para mostrarlo en crudo
print("""Primer linea
segunda linea
tercer linea""")
```

---

## :star: Boolean

Es le dato lógico, la minima unidad racional, su valor es: **verdadero** , **falso**.

Para ello utilizamos los operadores logicos : ``` < , > , <= , >= , ==, !=```

```Python
print(1+1 == 2) # True
print( 3 < 1) #False
```

A una variable tambien le podemos asignar el valor booleanos:
```Python
verdadero = True
falso = False
```

-> Los valores logicos siguen la logica proposicional : **and**, **or**

Para el caso de AND ambas deben ser True para tener True.

Para el caso de OR con que una sea True ya obtenemos True.

```Python
resultado1= ( 2 == 1+1) and ( 2 < 8) # True and True
print(resultado1) #True
resultado2 = ( 2 == 1+1) and ( 2 == 8) # True and False
print(resultado2) # False
resultado3 = ( 2 < 1+1) and ( 2 == 8) # False and False
print(resultado3) # False
print(type(resultado1)) #bool
```

---

## :star:  Comprobacion y converison de typos

Comprobacion de tipo de datos:

```Python
print(-1, type(-1)) # -1, <class 'int'>
print(3.1415, type(3.1415)) # 1.1415, <class 'float'>
print("hola", type("hola")) # hola , <'str'>
print(True, type(True)) # True, 'bool'
print(None, type(None)) #None <class 'NoneType'>
```

Conversion de Tipos -> CASTEO DE NUMBER A STRING
```Python
num=2
print(type(num)) #  <class 'int'>
num = str(num)
print(type(num)) # <class 'str'>
```

También se puede convertir sin asignar valor a una variable

```Python
print(int(2.1)) # castea a int (entero) : 2
print(int("2")) # castea a int(entero) : 2
print(int(True), int(False)) # castea a int (entero): 1 0
print(str(2)) # castea a string : 2
print(str(3.1415)) # castea a String : 3.1415
print(str(None)) #castea a String : None
```

---

## :star: Operadores aritmeticos y de asignacion

**+ es la suma**

```Python
print(8 + 30.5) # + hace la suma y como tengo int y float el resultado es float
print('Hola'+ ', como estas?') # el + en String concatena
```

**- es la resta**

```Python
print(49-30) # 19
```

**la multiplicacion es el estarisco**

```Python
print( 2*3.5) # 7
print("Turututu"*2) # el multiplicar por dos es lo mismo que sumar la cadena dos veces : TurututuTurututu
```

**/ es la division**
```Python
print( 10/4) # va a dar un float
print(10//2) # me va a mostrar el int de la respuesta
```

**% es el modulo**
```Python
print(10%2) # el modulo, me muestra el resto de la division
```
**doble asterisco es la exponenciacion**
```Python
print(2**3) # dos al cubo
```

## Operadores de asignacion

``` -= , += , *=, /= , //=, **=```

Se va a realizar la resta, suma, multiplicacion, division, potenciacion, etc y luego se asigna.

```Python
edad = 10
print(edad) # 10
edad -= 3
print(edad) #7
edad += 5
print(edad) # 12
edad /=2
print(edad) # 6
```

---

## :star: Operadores logicos

Estan relacionados con los boolean : True o False

```Python
print("-Se cumple que 2 > 3 \n", 2>3)
print("-Se cumple que 2 < 3 \n", 2<3)
print("-Se cumple que 2 != 3 \n", 2!=3)
```

Los operadores basicos de comparacion (<,>, <=, >=, =0, !=) tambien aplican a las cadenas de caracteres.

Para compararlas siguen el estandard ASCII
```
!"#$%&'()*+,-./
0123456789:;<=>?
@ABCDEFGHIJKLMNO
PQRSTUVWKYZ[\]_
`abcdefghijklmno
pqrstuvwxyz{|}
```

simbolos -> numeros -> comparacion -> simbolos -> letras

```Python
print("c" > "d") #False
```

Va a ir evaluando letra por letra, para el caso de que compara String

```Python
print("casa" > "cabra")
```

**AND**

Ambas deben ser verdaderas para que sea True, sino es False.


**OR**

Con que al mismo una sea verdadera, tendré True.

**NOT**

Niega el valor... 

...si tengo verdadero negado -> False

... si tengo falso negado -> True

---

## Lectura por teclado

Se realiza mediante la funcion **input()**

```Python
valor= input("Introduce un numero: ")
print(valor)
valor_numero_ingresado_flotante = float(input("Introduce un numero: ")) # asi lo casteo a flotante
edad_ingresada= int(input("Ingresa tu edad:"))  # para castearlo a entero
```

---

## Formateo

Puedo dejar espacios en cadenas de texto y luego defino que valor paso.

---
---