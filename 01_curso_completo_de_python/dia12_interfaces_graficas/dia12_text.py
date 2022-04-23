from tkinter import*

root=Tk()

root.title("Hi!")


texto = Text(root) # creo la variable texto y la ubico en el root
texto.pack()
texto.config(width=40, height=15, padx=15, pady=15, font=("Curier, 15"), selectbackground="yellow") # le doy un tamaño dando ancho y alto, no es pixeles, sino la cantida de caracteres. Y tambien un padding tanto en x como en y para despegarlo del borde al texto, tambien puedo agregar tipo de fuente y tamaño

label = Label(root, text="Escribe aqui:")
label.pack()
label.config(bg="red", fg="white", font=("Curier,20")) # le doy fondo rojo, color blanco, tipo de letra Curier y de tamaño 20

root.mainloop()