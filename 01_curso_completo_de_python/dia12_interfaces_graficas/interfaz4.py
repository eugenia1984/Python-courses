from tkinter import *

root=Tk()

root.title("Hi!")

imagen = PhotoImage(file="fondo.jpg") # las imagenes pueden ser .gif o .jpg y debe estar dentro de la carpeta raiz donde esta este archivo
label = Label(root, image=imagen)
label.pack()

root.mainloop()