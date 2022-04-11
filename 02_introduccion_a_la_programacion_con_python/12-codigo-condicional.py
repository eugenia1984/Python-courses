# CODIGO CONDICIONAL: cuando deseas que un código se ejecute de acuerdo a ciertas condiciones. Se utiliza el IF

"""
Ejemplo:
balance = 500

if balance > 0:
    print("Puede pagar")

OPERADORES QUE SE UTILIZAN PARA EVALUAR UNA CONDICIÓN:
== igual a
!= diferente a
> mayor a
>= mayor igual a
< menor
<= menor igual a
"""
# Revisar si una condición es mayor a
balance = 500

if balance > 0:
    print('Puedes pagar')  #se ejecuta porque la condición es True

# IF ELSE: si una condición es evaluada TRUE se ejecutará un código, pero a veces desas tener otra acción que se realice en caso de que la condición evaluada no se cumpla.

# Ejemplo de operador MAYOR: suponemos que alguien quiere pagar pero no tiene el saldo suficiente
balance2 = 0

if balance2 > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')

# Ejemplo de operador igual a:
likes = 200
if likes ==200:
    print('Excelente, 200 likes')    # prestar atención que para igualar se usa == y para asignar valor =

# Ejemplo de comparación con strings:
lenguaje  = 'Python'
if lenguaje == 'Python':
    print('Excelente decisión')

# Ejemplo de comparacón entre strings con no igual a:
lenguaje2 = 'Python'
if not lenguaje2 == 'Javascript':
    print('Es otro lenguaje')
#con el NOT negamos el True, nos pasa al valor contrario

# Ejemplo de Boolean:
usuario_autenticado = True

if usuario_autenticado: # Como es Boolean es True, por eso no se escribe if usuario_autenticado == True:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')



