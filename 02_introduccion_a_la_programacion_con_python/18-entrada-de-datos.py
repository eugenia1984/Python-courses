# ENTRADA DE DATOS: la mayoría del código que escribas tiene como fin solucionar un problema del usuario (publicar un muro, realizar un examen en línea, subir una imágen, solicitar un taxi, crear un evento, etc). En Python se utiliza la función input() para detener la ejecución del programa hasat que el usuario agregue información.
nombre = input('Cuál es tu nombre: \r\n ')
print(f'Hola {nombre}')

# Leer datos que serán numeros
edad = int(input('Cuál es tu edad? '))  #convertir la string a número

if edad >= 18:
    print('Puedes votar')
else:
    print('Aun no puedes votar')

# Mezclar con operadores
numero = int(input('Agrega un número y te diré si es par o impar: \r\n')) 
if numero % 2 == 0:
    print('Es un número par')
else:
    print('Es un número impar')




# DESAFIO: realizar un exámen con 3 preguntas que tu desees, el usuario deberá responder "SI" o "NO" y al final otorgarle una calificación (la calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1)

respuesta1 = (input('Debés responder con SI o NO: París está en Francia? \r\n')).upper() 
respuesta2 = (input('Debés responder con SI o NO: Se habla francés como idioma oficial en otro país además de Francia? \r\n')).upper() 
respuesta3 = (input('Debés responder con SI o NO: Limita Francia con Alemania? \r\n')).upper()

nota = 0

if respuesta1 == 'SI':
        nota+=1

if respuesta2 == 'SI':
        nota+=1

if respuesta3 == 'NO':
        nota+=1

print(f'Tu nota es un : {nota}')