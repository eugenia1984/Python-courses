# WHILE (se ejecuta mientras una condición es verdadera) y FOR (se ejecuta un determinado número de ocasiones según sean los elementos de una colección):  

# Ejemplo 1:
pregunta = 'Agrega un número y te diré si es par o impar \r\n'
pregunta += '(Escribe "cerrar" para salir de la aplicación): \r\n'
preguntar = True

while preguntar:
    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f'El número {numero} es par')
        else:
            print(f'El número {numero} es impar')
  
# Ejemplo 2:
numero2 = 0
while numero2 <= 10:
    print(numero2)
    numero2 += 1  #Incremento para evitar un Loop infinito

# IF DENTRO DEL WHILE
numero3 = 0
while numero3 <= 10:
    if numero3 ==5:
        print('CINCOOOOOO!!!')
          break
    else:
        print(numero3)
    numero3 += 1
 

