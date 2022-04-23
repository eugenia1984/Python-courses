from tkinter import *

root = Tk()

texto_nuevo = StringVar()
texto_nuevo.set("Python")

root.title("Hi!")
root.config(width=400, height=500)

label = Label(root, text="Hello world") # creo la etiqueta y le indico donde se ubica (root) y con text le indico que texto quiero ver
label.place(x=100, y=50) # porque si uso label.pack la ventana va a tomar el alto y ancho de mi label y no me respeta los 400x500 que le configure
label.config(bg="green", fg="white", font=("Curier",20)) # color de fondo verde , el color de letra blanco, la fuente le puedo determinar la familia y el tamaño

label = Label(root, text="Welcome")
label.place(x=110, y=150)
label.config(bg="red",font=("Curier",18), textvariable=texto_nuevo) # color de fondo rojo

root.mainloop()