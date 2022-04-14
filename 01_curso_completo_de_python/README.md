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

## Instalacion de Python

Desde [http:/www.python.org](http:/www.python.org) se descarga e instala Python.

---

## Numeros y variables

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

## Textos

```Python
print("Estoy 'aprendiendo' Python")
nombre="Maria Eugenia"
print("Buenas "+nombre) # para concatenar un String con una variable -> +
# con \t tabulo y con \n hago salto de linea
```

---

## Input

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

## Visual Studio Code

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

## Operadores relacionales

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


---
---