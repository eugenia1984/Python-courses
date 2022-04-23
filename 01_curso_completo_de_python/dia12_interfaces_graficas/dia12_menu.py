from tkinter import*

root=Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)
# creo la primer opcion del menu -> Archivo
archivoMenu = Menu(barraMenu, tearoff=0) #  tearoff=0 para no tener los ---- separadores
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
# creo las tres opciones del submenu
archivoMenu.add_command(label="Nuevo Archivo") 
archivoMenu.add_command(label="Nueva Ventana") 
archivoMenu.add_separator() # va a ser la barra separadora
archivoMenu.add_command(label="Salir")  

# creo la segunda opcion del menu -> Editar
archivoEditar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEditar)
# creo las opciones de submenu
archivoEditar.add_command(label="Deshacer")
archivoEditar.add_command(label="Rehacer")

#creo la tercer opcion de menu -> Ayuda
archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
# creo los opciones del submenu
archivoAyuda.add_command(label="Acerca de...")
archivoAyuda.add_command(label="Licencia")

root.mainloop()