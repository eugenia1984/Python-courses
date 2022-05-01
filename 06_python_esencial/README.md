# :book: Python Esencial - Curso de LinkedIn Learning de Ana María

---

## Historia

- Creado por Guido Van Rossum

- Fue lanzado en 1191

- El nombre se inspira en la serie de Monty Python Flying Circus

- BSFL: Banavolent Dictator for Life

---

## Programación para todas las personas

- fácil e instuitivo

- open source

- fácil de interpretar en inglés

- apto para las actividades diarias

---

## Principios:

- bonito es mejor que feo -> mejor exribir ordenado y facil de entender

- explicito es mejor que implícito -> el codigo por si mismo debe explicar lo que hace

- simple es mejor que complejo -> siempre que pueda hacerse censillo, hacerlo sencillo

- complejo es mejor que complicado -> hacer algo complejo facil de entender en vez de algo complicado que nadie entinedo

---

## Python 3

Es la versión actual, desde 2020.

---

## Python en la industria:

- ciencia y analítica de datos

- inteligencia artificial

- desarrollo web

---

## Consola o terminal

- interfaz de usuario

- funciona a través de instrucciones o comandos

- sin interfaz gráfica

Python es un lenguaje de programación sin interfaz gráfica. Pero con Python podemos crear aplicaciones de consola o escritorio.

Para correr Python lo podemos hacer desde **consola** / **terminal** o con un IDE como el **Visual Studio Code**.

Para entrar a la CONSOLA o SHEL de Python en la terminal escribimos **Python**.

---

## PEP8 es la guia de estilos de Python

Algunas cosas:

- identación, es muy importante para separar bloques de codigo ya que no hay () ni {}, por convension se dejan 4 espacios para identar.

- tamaño maximo de una linea de codigo de 79 caracteres, para que sea legible el codigo

- 2 lineas en blanco para...

... separar funciones o clases

- 1 linea en blanco para...

... separar los métodos de una clase

... al final de cada archivo

... para separar las lineas de codigo que cumplen diferentes areas

---

## Estructuras de datos

- forma de organizar los datos

- permite manipular extraer, buscar e insertar datos

- son eficientes, porque reducen el tiempo de procesamiento

- son mutables si sus elementos pueden ser modificados después de ser creados.

 ### Tipos de estructuras de datos en Python

 - **Listas**,  sus elementos están entre **[]** y pueden tener elementos duplicados

 - **Tuplas**, sus elementos entre **()** y pueden tener elementos duplicados

 - **Diccionarios**, se definen entre **{}** y cada elemento es una combinacion de **llave:valor**

 - **Sets**, se definen entre **[]** y se diferencian porque sus elementos son unicos, no pueden repetirse.

 Una estructura es ORDENADA cuando sus elementos mantiene el mismo orden en el que fueron definidos

 Son MUTABLES cuando pueden ser modificados en el tiempo

 | - | Lista | Tupla | Set | Diciconario |
 | - | ----- | ----- | --- | ----------- |
 | ordenado | si | si | no | no |
 | mutable | si | no | si | si |
 | permite duplicados | si | si | no | no |



---

En el archivo **02_estructuras_de_datos.py** estan todas las estructuras: listas, tuplas, diccionarios, sets

---

## Condiciones y Ciclos

- Las condiciones son instrucciones que se ejecutan o no al cumplirse una condición

- dependen de una condicion logica y se usan para comparar, con: == , !=, < , >, >=, <=

- retornan una variable booleana

- **is** para evaluar si dos variables son el mismo objeto

- **and** para unir dos o mas condiciones, solo es true si TODAS es true

- **or** para unir condiciones, con que al menos tenga una true, entonces la sentencia completa es true

- **not** es la negacion


## IF - ELSE
```
     ----------condicion------------
     |                              |
  no se                            se
  cumple                         cumple
     |                              |
     v                              v
  bloque                         bloque
   else                            if
     |                              |
     ------> instruccion <----------         
```

## IF - ELIF - ELSE
```
if <condicion logica>:
   print("if block")
elif <condicion logica>:
   print("elif block")
else:
   print("else block")
```

## Ciclos

- Instruccion que se repite hasta que se cumple una condicion

- Tipos de ciclos: for, while

```
             | 
             v
--------> Instruccion
|            |
|            v
|        ¿Repetir? -- no se cumple--> Instruccion
|            |
--se cumple---
```


### CICLO FOR

**object** puede ser lista, tupla, set, diccionario

**element** es cada posicion de esa estructura

Tambien podemos iterar en objetos de tipo String

```
for <element> in <object>:
   print("Elemento:" <element>)
```

## CICLO WHILE


Mientras se cumpla al condicion se ejecuta, tiene que llegar un momento en que la condición no se cumpla, sino estoy en un loop infinito

```
while <condicion>:
   print("ciclo while")
```

---

## FUNCION RANGE

```Python
for element in range(5):
  print(element)
"""
0
1
2
3
4
"""
```

Con dos parametros le indico el punto de partida y el de finalizacion, no incluye el ultimo numero

```Python
for element in range(1, 5):
  print(element)
"""
0
1
2
3
4
"""
```

---
---

## funciones

- bloque de codigo

- contiene instrucciones relacionadas que realizan una tarea

Ventajas:

- organizan el codigo en partes pequeñas

- permiten mantener el codigo ordenado y facil de entender

- evita la repeticion de instrucciones y permite reusarlo

## Definicion

Con la sentencia **def**

```
def <nombre funcion>():
  <instruccion>
```

## Invocacion

```
<nombre funcion>()
```

### Tipos de funcions

- built-in fucntion, ya vienen con python, como print()

- user-defined functions, yas funciones que creamos


Las **variables locales** solo existen dentro de la funcion

```Python
def funcion():
  print("Mi primera funcion")
  nombre= "Eugenia"
  print(nombre)

funcion() 
# Mi primera funcion
# Eugenia
# si quiero imprimir nombre fuera de la funcion voy a tener error
```

Las **variables globales** se pueden utilizar en todo el programa, se suelen declarar al principio y luego van las funciones, van en mayuscula

```Python
APELLIDO = "Costa" # variable global
def funcion():
  print("Mi primera funcion")
  nombre ="Maria Eugenia" # variable local
  print(nombre, APELLIDO)

funcion() 
# Mi primera funcion
# Maria Eugenia Costa
```

## Parametros

Los parametros de una funcion son los valores que reciben

```Python
def perimetro_cuadrado(lado, unidades):
  perimetro = lado * 4
  print(f"El perimetro es {perimetro} {unidades}")

perimetro_cuadrado(4, "cm") # El perimetro es 16 cm
```

El **argumento** hace referencia al valor que entra en la funcion


## Retorno de valores en una funcion de Python

```Python
def perimetro_cuadrado2(lado): # funcion con return
  perimetro = lado *4
  return perimetro
```

Se puede retornar más de un valor, en este caso se separa con COMa y devuelve uuna TUPLA

## Documentacion de una funcion en Python

Nos permite entender la funcion, que parametros recibe, que retorna

Se llama **DOC STRING**

``` """ """ ``` documentacion simple

documentacion larga:

```Python
def calcular_cuadrado_perimetro(lado):
  """Calcular el perimetro de un cuadrado:
  
  Esta funcion recibe el valor del lado de un cuadrado
  y a partir de este calcula y retorna su perimetro
  
  Args:
      lado (int): medida del lado del cuadrado

  Returns:
  perimetro (int): perimetro dle cuadrado
  """
  perimetro = lado *4
  area = lado * lado
  return area, perimetro
```

---
---

## Modulos


Son otros archivos Python que tiene una o varias funciones.

Los **paquetes** son carpetas que contienen **modulos** y permiten tener en orden el proyecto.

Los **paquetes** deben contener un **archivo de inicialización** llamado **init**.

Las **librerías** de Python son **paquetes** desarrollados por la comunidad para diferentes aplicaciones, un ejemplo es Pandas (para manipular datos).

### Importación de módulos y paquetes en Python

Al **importar** una librería podemos utilizar las **funciones** que tiene la misma.

Al algunas librerías que ya viene incluídas en la instalación de Python.

Para importar una librería utilizamos la sentencia **import**.


Ejemplo de importación de la librería **datetime**, utillizando el alias **as** de **dt**:
```Python
import datetime as dt

hora_actual = dt.datetime.now()
print(hora_actual)
```

También tenemos la insstrucción **from** para importar un único **submodulo** sin tener que importar la librería completa.

Por ejemplo:

```Python
from datetime import datetime

hora_actual = datetime.now()
import(hora_actual)
```

## Creo mi primer modulo

Lo llamo **cuadrado.py** que me permite calcular el area y el perimetro de un cuadrado.


```Python
def area_cuadrado(lado):
  return lado * lado

def perimetro_cuadrado(lado):
  return lado * 4
```

Y en el archivo : **07_main.py** voy a importar y utilizarlo:

```Python
from figuras.cuadrado import area_cuadrado, perimetro_cuadrado

lado = 5
cuadrado = {
  "lado": lado,
  "area": area_cuadrado(lado),
  "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado) # {'lado': 5, 'area': 25, 'perimetro': 20}
```

## Creando un paquete en Python

Son colecciones o conjuntos de módulos que se guardan dentro de una misma carpeta.

LOs paquetes alamcenan módulos cuyas funciones son comunes entre sí.

Vamos a crear un paquete de figuras geométricas, para lo cual creamos la carpeta **figuras** y dentro de la misma tenemos el archivo **__init__.py** lo que indica que es un paquete con modulos.

Cómo primer módulo utilizaremos **cuadrado.py**, **circulo.py**:

```Python
# CIRCULO
def area_circulo(radio):
  return 3.14 * radio * radio

def perimetro_circulo(radio):
  return 3.14 * 2 * radio
```

Fuera de la carpeta figuras, creo el archivo **08_main.py**, el archivo principal donde importaré las funciones del paquete figuras:

```Python
from figuras.cuadrado import *
from figuras.circulo import *

lado = 4
cuadrado = {
  "lado": lado,
  "area": area_cuadrado(lado),
  "perimetro": perimetro_cuadrado(lado)
}

radio = 5
circulo = {
  "radio" : radio,
  "area" : area_circulo(radio),
  "perimetro": perimetro_circulo(radio)
}

print("Cuadrado: ", cuadrado) # Cuadrado:  {'lado': 4, 'area': 16, 'perimetro': 16}
print("Circulo: ", circulo) # Circulo:  {'radio': 5, 'area': 78.5, 'perimetro': 31.400000000000002}

```

---
---

## POO

Es un paradigma de programación donde todos los datos son **objetos**, lo que nos permite simplificar los problemas cuando representamos y modelamos cosas de la vida real.

**objeto** -> elementos o **instancias** que se crean a travès de una clase. Tienen **atributos** (caracteristicas que definen al objeto) y **metodos** (funciones).

Tienen 4 pilares:

**abstracción** : define las características y funcionalidades de un objeto (es como un plano a partir del cual se contruye el objeto).

**encapsulamiento** : evita que los objetos se manipulen de manera incorrecta.

**herencia** : se crea un hijo a partir de un padre, y este hereda sus características y funciones.

**polimorfismo** : ante la misma función, el objeto hijo puede responder distinto que el padre. 


## Clases e instancias en Python

Una clase se declara con la palabra reservada **class** y el nombre se escribe en **CamelCase**, creo el archivo **09_persona.py**:


```Python
class Persona:
  pass

pedro = Persona()
print(type(pedro)) # <class '__main__.Persona'>

paco = Persona()
print(type(paco)) # <class '__main__.Persona'>

print(pedro == paco) # False, porque los objetos son de igual tipo pero cada uno ocupa un lugar diferente en la memoria de la computadora, por lo que no son el mismo objeto
```


## Constructor de una clase en Python


Define las propiedades del objeto y sus metodos, es la función **__init__**, tengo el archivo **10_persona.py**.

Como primer parámetro va a recibir **self**, la variable que representa la instancia de la clase, y a traves de ella se pueden acceder a las propiedades y funciones de la misma.

```Python
class Persona:
  def __init__(self):
    print("Estoy en el constructor")

paco = Persona()
print(paco) # Estoy en el constructor
```

O sea que cuando se instancia un nuevo objeto se ejecuta el método constructor


## Atributos de una clase en Python

Los atributos son las propiedades de una clase, las variables que definen la característica de un objeto.


Los atributos pueden ser de dos tipos...

... **se instancia** se definen dentro de la funcion init


... **de la clase**, variables que se definen por afuera del constructor y tiene el mismo valor para todos los objetos que se crean a partir de esa clase


Creo el archivo **11_persona.py**:

```Python
class Persona:
  atributo = 123

  def __init__(self, nombre, edad):
    """Funcion constructora"""
    self.nombre = nombre
    self.edad = edad

paco = Persona('Paco', 20)
print(paco.nombre) # Paco
print(paco.edad) # 20
print(paco.atributo) # 123
```

Al crear la clase con sus atributos e instanciar un objeto con atributos ya puedo acceder a los mismos.


## Metodos de una clase

Son funciones que se definen dentro de una clase y cada uno de los objetos creados a partir de una clase puede acceder a sus métodos.

Los métodos de las clases se definen como las funciones, con la difernecia de que los métodos reciben como primer atributo la variable **self** que representa al instancia de la clase y através de ella se puede acceder a las propiedades y funciones de la clase.


Creo el archivo **12_persona.py**:

```Python
class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def cumplir_anios(self):
    self.edad += 1
    print(f"Feliz cumpleaños número {self.edad} {self.nombre}")

paco = Persona ('Paco', 20)
print(paco.cumplir_anios()) # Feliz cumpleaños numero 21 Paco
```

## Herencia de clases en Python

Permite que una clase sea creada a partir de otra. Hay una **clase Padre**, la clase principal y una clase secundaria, **clase hijo** que hereda las característica y los atributos de la clase padre; lo que nos permite reutilizar código ya existente.

La clase padre y la clase hija deben estar relacionadas entre sí.

Teniendo ya mi clase **Persona** que va a ser mi clase padre voy a crear la clase **Empleado**.

Creo el archivo **13_herencia.py**:

```Python
class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def cumplir_anios(self):
    self.edad += 1
    print(f"Feliz cumpleaños número {self.edad} {self.nombre}")

class Empleado(Persona):
  """La clase Empleado extiende de Persona"""
  def trabajar(self, horas_trabajadas):
    print(f"Usted ha trabajado: {horas_trabajadas} horas")

paco = Empleado('Paco', 20)
print(paco.cumplir_anios()) # Feliz cumpleaños numero 21 Paco
print(paco.trabajar(100)) # usted ha trabajado: 100 horas
```

A la clase **Empleado** le agrego atributos propios de su clase, como **horas_totales**:

Con **super()** llamo al constructor de la clase padre
```Python
class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def cumplir_anios(self):
    self.edad += 1
    print(f"Feliz cumpleaños número {self.edad} {self.nombre}")

class Empleado(Persona):
  """La clase Empleado extiende de Persona"""
  def __init__(self, horas_totales, nombre, edad):
    """con super() hereda lso atributos de la clase persona, si no esta voy a sobreescribir el metodo constructor y no heredo los atributos de la clase Padre"""
    super(Empleado, self).__init__(nombre, edad)
    self.horas_totales = horas_totales

  def trabajar(self, horas_trabajadas):
    self.horas_totales = horas_trabajadas
    print(f"Usted ha trabajado: {horas_trabajadas} horas")
    print("Horas totales: ", self.horas_totales)

paco = Empleado(nombre='Paco', edad=20, horas_totales=200)
print(paco.cumplir_anios()) # Feliz cumpleaños numero 21 Paco
print(paco.trabajar(horas_trabajadas=8)) 
# Usted ha trabajado: 8 horas
# Horas totales:  8
```


```Python

```



---
---

## Ambientes virtuales

### Paquetes de Python

En su mayoría las podemos encontrar en la pagina de **PyPI**, **Python Package Index** que es el repositorio de paquetes y librerías de python

Su página es **pypi.org**

**Numpi** es una de las librerías más usadas para operaciones matemáticas y análisis de datos

### Instalación de paquetes con Pip

Se hace con el comando **pip** , se usa tanto para instalar como para actualizar uan librería.

Este comando de hace desde la consola, no desde la shell de Python.


Para verificar que tenemos pip:
```> pip --version```

Para instalar un paquete:
```> pip install <libreria a instalar>```

Si queremos instalar una version específica:

```> pip install <nombre de la libreria>==<numero de la version> ```, por ejemplo: ```> pip install pandas==1.3.4 ```

Al final tengo el aviso si se instaló correctamente

Con pip también está la instruccion **freeze**, y veo una lista de las librerías instaladas en este momento.

```> pip freeze```

En el caso de t¡necesitar **desinstalar** un paquete o una librería:

```> pip uninstall <nombre de la libreria> ```, por ejemplo: ``` > pip install pandas```


### Introducción a ambientes virtuales

Son desarrollo aislado que creamos para cada proyecto que estemos desarrollando, estos ambientes contienen unicamente los paquetes necesarios para el proyecto.

Sus ventajas:

- independencia entre proyectos

- manejo de diferentes paquetes y versiones entre proyectos

- facilidad de borrar paquetes en caso de conflictos

Librerías para ambientes:

- virtualenv

- Venv

- Anaconda

## ¿ Cómo crear un ambiente virtual usando virtualenv ?

Es bastante estable y compatible con una gran cantidad de librerías.

Para **instalarlo**: ```> pip install virtualenv ```

Los ambientes con virtualenv se crean dentro de la carpeta donde estamos ubicados, por eso se recomienda que para cada proyecto se tenga un ambiente propio.

Para **crear un ambiente** : ```> virtualenv <nombre del ambiente>```, por ejemplo ```> virtualenv env``` y ahora tengo una carpeta llamada **env**, donde tengo el ambiente.

Para **activar el ambiente**: ```>env\Scripts\activate ``` vamos a ver en el path delante **(env)**

Para **mac** o **linux**: ```source env/bin/activate```

Para **desactivar el ambiente** con : ```> deactivate``` y ya en el path no vamos a tener entre () el nombre del ambiente.

Si necesitamos **borrar el ambiente**: ```> rmdir env /s```, mara **mac** o **lunx** es ``` rm -f env```


### Archivo de requerimientos para proyectos de Python

Es un archivo de texto plano que se crea con el fin de tenr en una lista todas las librerías que se requieren para un proyecto, nos permite que todas las personas involucradas tengan las mismas versiones de las librerías y no existan conflictos entre los desarrolladores y los ambientes de desarrollo.

Creamos el archivo: **requirements.txt**, por estandar se utilliza este nombre.

```
flask==2.0.
```

No es necesario que en el archivo las librerías tienen la versión, pero es recomendable especificarlo para evitar conflicto de paquetes en el futuro.

Para instalar las librerias de requerimineto, por terminal:

```> pip install -r requirements.txt```

Y en la terminal vemos que los paquetes se instalan y descargan

Una vez que esta todo ok: ``` > pip freeze``` que muestra todos los paquetes instalados, algunas instalamos a través del archivo de requerimientos, otras vienen instaladas con nuestro ambiente y otras son las dependencias de las librerías que instalamos del archivo requeriments.txt
---
---

## Errores y excepciones

### Que son los errores y las excepciones

Es importante que el programa sea a prueba de errores.

En Python hay distintos tipos de errores, como por ejemplo...

... **error de sintaxis** cuando escribimos mal, por ejemplo nos olvidamos un parentesis.

... **error por variable no definida**, cuando llamamos a una variable sin antes haberla creado.

... **error al dividir por cero**

... **error por tipo de dato**, por ejemplo al sumar un string con un numero



En Python existen dos tipos de errores:

- errores de sintaxis, cuando escribimos mal una sentencia

- las excepciones, cuando auqnue las instrucciones están escritas de manera correcta generar un error (como la division por cero, variable no definida, eror por tipo de dato). Ocurren durante la ejecución del programa.

### Errores de sintaxis en Python


Hacen referencia a los errores que ocurren en Python cuando una instrucción está mal escrita.

Al ejecutar el programa aparece que el tipo de error es **SyntaxError**, un ejemplo:

```Python
print"hola"
```

Por que no incluí los paréntesis, me indica la linea donde tengo el error.

Si utilizo VSC voy a tener una linea que me marca el error.

Para evitar errores de sintaxis, hay que tener en cuenta:

- no usar palabras reservadas como nombres de variables

- asegurarse que los bloques de codigos esten con :

- asegurarse de estar bien identados

- cuando escribir variables de texto hay que abrir y cerrar con el mismo tipo de comillas

- asegurarse de cerrar, parentesis, llaves o corchetes en las estructuras de datos que se utilizano en las sentencias que lo requieran


### Levantar exepciones en Python

Se pueden programar desde el codigo usando **Raise Exception**, para cuando queremos que al cumplir una condición nuestro código termine en un error.

Para mostrar un ejemplo crearemos una función para validar un número, si el número es menor a 1 la función levantará una excepción e iprimirá un mensaje. Si el número es mayor se imprimirá un mensaje, sin levantar ningún tipo de error.

Creo el archivo **_exception.py**:

```Python
def validar_x(x):
  if x<1:
    raise Exception("La variable x debe ser mayor a 1")
  else:
    print("x es mayor a 1")

x = 0.3
validar_x(x) # Exception: La variable x debe ser mayor a 1
x = 2
validar

### Assertion Error en Python

### Try-Except para el manejo de excepciones en Python

---
---
