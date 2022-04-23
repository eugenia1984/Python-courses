from tkinter import *

root=Tk() # creo la ventana
root.title('Hola') 
root.resizable(1, 1) 
# creo el Frame e indico esta dentro de la raiz (root)
miFrame = Frame(root) 
miFrame.pack(fill="x", expand=1) 
miFrame.config(width=400, height=600) # le doy un ancho y alto
miFrame.config(cursor="boat") # para darle un cambio de cursor, cuando pase el mouse por el Frame se hace un barco, otro es el "pirate"
miFrame.config(bg="red") # para cambiar el color de fondo bg= background
miFrame.config(bd="20") # para indicarle un tamaño a un borde
miFrame.config(relief="sunken") # para ver un tipo de borde, otro metodo es "ridge"
# este mismo metodo se puede aplicar al root
root.config(cursor="pirate")
root.config(bg="white") 
root.config(bd="10")
root.config(relief="ridge") 

root.mainloop() # para mantener la ventana abierta .mainloop() debe estar por debajo del contenido que le agregamos a la ventana

