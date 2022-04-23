from tkinter import*

# Voy a agrupar aca mis funciones
def sumar(): # la funcion que me va a calcular la suma
  resultado.set(int(var1.get())+int(var2.get()))
def restar(): # la funcion que me va a calcular la resta
  resultado.set(int(var1.get())-int(var2.get()))
root = Tk()

frame= Frame(root)
frame.pack()

# Creo tres variables dinamicas para ponerlas en cada una de las entry
var1= StringVar()
var2 = StringVar()
resultado = StringVar()

entrada1 = Entry(frame) # creo la primer entrada
entrada1.pack()
entrada1.config(bd=10, font=("Curier 20"), textvariable=var1)

entrada2 = Entry(frame) # creo la segunda entrada
entrada2.pack()
entrada2.config(bd=10, font=("Curier 20"), textvariable=var2)

entrada3 = Entry(frame) # creo al tercer entrada
entrada3.pack()
entrada3.config(bd=10, font=("Curier 20"), state="disable", textvariable=resultado) # lo deshabilito porque acaa quiero mostrar el resultado, no quiero que puedan ingresar nada y le agrego la varaible del texto dinamico

boton1 = Button(frame, text="Sumar") # creo el boton1 que esta en el frame y tiene el texto Sumar
boton1.pack()
boton1.config(bd=5, font=("Curier 10"), command=sumar) # le agrego un borde y cambio la fuente y tamaño de la letra y la funcion sumar

boton2 = Button(frame, text="Restar") # creo el boton2 que esta en el frame y tiene el texto Restar
boton2.pack()
boton2.config(bd=5, font=("Curier 10"), command=restar) # le agrego un borde y cambio la fuente y tamaño de la letra y la funcion restar

root.mainloop()