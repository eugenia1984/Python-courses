from tkinter import*

root= Tk()

root.title("Hi!")# le cambio la etiqueta
frame = Frame(root, width=500, height=400) # creo un Frame y le doy ancho y alto
frame.pack()

entrada_nombre = Entry(frame) # creo la variable entrada_nombre que va a guardar mi Entry del nombre ingresado
entrada_nombre.grid(row=0, column=1, sticky="n", pady=10) # la empaqueto y ubico en grilla , con sticky lo ubico pegado hacia el norte, al borde top y le agrego un padding top de 10px
entrada_nombre.config(justify="center") # asi centro el texto en el medio y comienzo a escribir desde el medio 

entrada_apellido = Entry(frame) # creo la variable entrada_apellido que va a guardar mi Entry del apellido que ingrese
entrada_apellido.grid(row=1, column=1) # la empaqueto y ubico en grilla

label_nombre = Label(frame, text="Nombre: ") # creo el label para el texto nombre
label_nombre.grid(row=0, column=0, padx=5, pady=5) # Lo ubico por grid diciendo en que fila y columna estara, y tambien le agrego padding left y right con padx y padding top y bottom con pady

label_apellido = Label(frame, text="Apellido: ")
label_apellido.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()