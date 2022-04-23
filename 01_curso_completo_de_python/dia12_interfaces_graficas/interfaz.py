from tkinter import *

root=Tk() # creo la ventana
root.title('Euge') # asi modifico el titulo
# quiero darle un tamaño fijo de ancho y alto y que el usuario no manipule si tamaño
root.resizable(0, 0) # no se puede cambiar ni a lo ancho ni a lo alto de la ventana
# para cambiar el icono de la pluma que viene por defecto
# root.iconbitmap("pulpo.ico")




root.mainloop() # para mantener la ventana abierta, debe estar por debajo del contenido que le agregamos a la ventana