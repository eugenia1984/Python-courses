# ITERADORES: Aalgunas veces desearás correr el mismo código determinado número de ocaciones hasta que una condición se cumpla (o deje de cumplir). Se usan bastante en base de datos.

# Iterador (corre determinado número de ocaciones el código)
lenguajes = ["Python", "Kotlin", "Java", "JavasScript", "Ruby", "GO"]
for lenguaje in lenguajes:
    print(f'Estoy aprendiendo {lenguaje}')

# For que escriba números (corre mientras esté en el rango)
for numero in range(0, 20, 2):
    print(numero)       # El 20 no lo imprime porque está en el límie del rango, el 2 es el step -incremente de 2 en 2-