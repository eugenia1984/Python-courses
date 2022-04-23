from tkinter import*
from tkinter import messagebox

# creo la funcion para salir
def salir():
  # .askquestion es para que salte la consulta, y recibe param1 es el titulo, param2 es la pregunta
  i= messagebox.askquestion("Salir", "¿Esta seguro que desea salir?") 
  # ahora tengo que evaluar si el usuario quiere salir o no
  if i == "yes":
    root.destroy() # asi se cierra la ventana emergente
# creo la funcion para cuando hacen click en Acerca de ...
def acerca():
  # con .showinfo voy a mostrar informacion
  i = messagebox.showinfo("Informacion", "Creado por Maria Eugenia Costa")
  return i
# creo la funcion para el menu con opcion licencia
def licencia():
  messagebox.showinfo("Licencia", "Producto licenciado hasta 2070")
# funcion para que cuando uno quiera abrir una nueva ventana salga un error
def error():
  messagebox.showerror("Error", "Se ha producido un error fatal")
# funcion para la opcion deshacer del menu
def deshacer():
  messagebox.askquestion("¿Estas seguro?", "¿Desea deshacer todo?")
  
root=Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)
# creo la primer opcion del menu -> Archivo
archivoMenu = Menu(barraMenu, tearoff=0) #  tearoff=0 para no tener los ---- separadores
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
# creo las tres opciones del submenu
archivoMenu.add_command(label="Nuevo Archivo") 
archivoMenu.add_command(label="Nueva Ventana", command=error) 
archivoMenu.add_separator() # va a ser la barra separadora
archivoMenu.add_command(label="Salir", command=salir)   # command=salir para la ventana emergente

# creo la segunda opcion del menu -> Editar
archivoEditar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEditar)
# creo las opciones de submenu
archivoEditar.add_command(label="Deshacer", command=deshacer)
archivoEditar.add_command(label="Rehacer")

#creo la tercer opcion de menu -> Ayuda
archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
# creo los opciones del submenu
archivoAyuda.add_command(label="Acerca de...", command=acerca)
archivoAyuda.add_command(label="Licencia", command=licencia)

root.mainloop()