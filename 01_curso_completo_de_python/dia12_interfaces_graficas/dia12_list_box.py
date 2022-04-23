from tkinter import*

root =Tk()

root.geometry("400x400")

productos = Label(root, text="Productos") # creo un label con el texto Productos
productos.pack()

def agregar(): # funcion para agregar productos
  listaProductos.insert(END, entrada.get()) # con ENd voy a ubicarlo al final de la lista

listaProductos = Listbox(root, width=50) # creo mi lista
listaProductos.insert(0, "Carne")  # con.insert() agrego el producto, con el 0 indico en que indice se encontrara
listaProductos.insert(1, "Pollo")
listaProductos.insert(2, "Verdura")
listaProductos.insert(3, "Jugo")
listaProductos.pack()

listaProductos.delete(0) # Eliminar productos con .delete()

# Agregar productos
entrada = Entry(root, bd=10)
entrada.pack()

boton = Button(root, text="Agregar producto:", bd=10, command=agregar)
boton.pack()

root.mainloop()