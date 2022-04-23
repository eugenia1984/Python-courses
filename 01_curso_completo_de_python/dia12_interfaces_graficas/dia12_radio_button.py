from tkinter import*
def mostrar():
  if opciones.get() == 1:
    label2.config(text="Has elegido Masculino")
  elif opciones.get() == 2:
    label2.config(text="Has elegido Femenino")
  elif opciones.get() == 3:
    label2.config(text="Has elegido Binario")
  else:
    label2.config(text="Prefieres no contestar")

root=Tk()

opciones = IntVar()

label1 = Label(root, text="Elige tu genero: ")
label1.pack()
label1.config(bg="yellow")
Radiobutton(root, text="Masculino", variable=opciones, value=1, command=mostrar).pack() # creo un radio button, lo ubico en root, y con el texto Masculino. lo empaqueto
Radiobutton(root, text="Femenino", variable=opciones, value=2, command=mostrar).pack() # creo un radio button, lo ubico en root, y con el texto Femenino. lo empaqueto
Radiobutton(root, text="Binario", variable=opciones, value=3, command=mostrar).pack() # creo un radio button, lo ubico en root, y con el texto Binario. lo empaqueto
Radiobutton(root, text="Prefiero no contestar", variable=opciones, value=4, command=mostrar).pack() # creo un radio button, lo ubico en root, y con el texto Prefiero nno contestaro. lo empaqueto

label2 = Label(root)
label2.pack()
label2.config(bg="yellow", padx=10, pady=10)

root.mainloop()