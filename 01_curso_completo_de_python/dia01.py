i = 10 # declaro una variable y le asigno valor, en este caso es un int (INTEGER / ENTERO)
i = i + 20 # i = 30
division = i/30  # en este caso el valor de division es FLOAT (decimal)
print(division)
resta = i - 2
print(resta)
multiplicacion = i*2
print(multiplicacion)
potenciacion = i**3
print(potenciacion)
# Strings
print("Estoy 'aprendiendo' Python")
nombre="Maria Eugenia"
print("Mi\tnombre es "+nombre) #concateno String con variable, con \t tabulo y con \n hago salto de linea
entrada1 = input ("Introduce un dia de la semana : ") # va a entrar como String
entrada2 = int(input ("Introduce un numero : ")) # va a entrar como String y se castea a int

# TAREA
# 1- Escribir un programa que muestre por pantalla la cadena Hola mundo!
saludo = "Hola mundo!"
print(saludo)

# 2- Escribir un programa que guarde en variable la cadena Estoy aprendiendo Python! Y que luego muestre en pantalla el valor de la variable
aprendiendo = "Estoy aprendiendo Python!"
print(aprendiendo)

# 3-Escriba un programa que le pregunte al usuario su nombre para luego saludarlo por consola con su nombre
nombre_ingresado = input("Ingresa tu nombre: ")
print("Hola " + nombre_ingresado)
# 4- Defina tres variables: una que reciba un valor flotante, un valor entero y un String
calor_flotante = 15.67
valor_entero = 10
valor_cadena = "Estamos en feriado"