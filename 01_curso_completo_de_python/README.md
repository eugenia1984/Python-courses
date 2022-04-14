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

 ## :star: Días 1

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

Desde [http://www.code.visuastudio.com](http://www.code.visuastudio.com) descargo Visual Studio Code y le agrego la extension de Python de Microsoft