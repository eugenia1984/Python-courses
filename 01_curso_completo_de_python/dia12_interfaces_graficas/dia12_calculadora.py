from tkinter import*

root=Tk()
root.title("Mi calculadora")

# Entrada
entrada = Entry(root, font=("Curier 20"))
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botones
boton1 = Button(root, text="1", width=5, height=5)
boton2 = Button(root, text="2", width=5, height=5)
boton3 = Button(root, text="3", width=5, height=5)
boton4 = Button(root, text="4", width=5, height=5)
boton5 = Button(root, text="5", width=5, height=5)
boton6 = Button(root, text="6", width=5, height=5)
boton7 = Button(root, text="7", width=5, height=5)
boton8 = Button(root, text="8", width=5, height=5)
boton9 = Button(root, text="9", width=5, height=5)
boton0 = Button(root, text="0", width=13, height=5)

boton_borrar = Button(root, text="DEL", width=5, height=5)
boton_parentesis_abre = Button(root, text="(", width=5, height=5)
boton_parentesi_cierra = Button(root, text=")", width=5, height=5)
boton_punto = Button(root, text=".", width=5, height=5)

boton_division = Button(root, text="/", width=5, height=5)
boton_multiplicar = Button(root, text="*", width=5, height=5)
boton_sumar = Button(root, text="+", width=5, height=5)
boton_restar = Button(root, text="-", width=5, height=5)
boton_igual = Button(root, text="=", width=5, height=5)

root.mainloop()