#ELIF: if...elif...else, para cuando quieres evaluar una condición u otra y realizar diferentes acciones según sea el caso.

#Ejemplo:
ocupacion = 'Estudiante'

if ocupacion == 'Estudiante':
    print('Tienes 50 % de descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75 % de Desceunto')
else:
    print('Debes pagar el 100%')

# Se evalúa la primera condición y ejecuta si es True, sino pasa a la segunda condición y se ejecuta si es verdadera, sino para a la otra condición, y así sigue hasta encntrar la que sea True, salvo que ningua se cumpla y cae en el ELSE