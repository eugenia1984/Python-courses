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

--

## Operador logico

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

## Operadores de asignacion

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

Para alterar el flujo natural del programa tenemos las **condicionales**

```Python
edad = 20
if edad >=18:
  print("Es mayor de edad")
```

Solo si la condición dentro del **if** es True ( se cumple), se entra dentro del bucle, si no cumple (si es False) entonces nunca entrará.

---

## Bucles

Nos permiten repetir una porción de código tantas veces como queramos o necesitemos.

### While

Si **edad2** no estuviera cambiando en cada iteracion -> estaría en un bucle infinito

Es muy importante que la variable vaya cambiando de valor y en algún momento la condición pasa de True a False, para cortar el loop

```Python
edad2 = 1
while edad2 <=18:
  print("Es menor de edad")
  edad2+=1
```

--- 