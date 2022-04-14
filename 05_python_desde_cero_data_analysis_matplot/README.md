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


**Neww** -> **python 3** para abrir un nuevo archivo

**quit** para salir


---

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