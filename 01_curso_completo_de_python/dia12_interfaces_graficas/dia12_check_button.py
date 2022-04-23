from tkinter import*

# la funcion para evaluar
def eleccion():
  elegir=""
  if pollo.get()==1:
    elegir+=" Has elegido Pollo\n"
  if pizza.get()==1:
    elegir+=" Has elegido Pizza\n"
  if hamburguesa.get()==1:
    elegir+=" Haz elegido Hamburguesa\n"
  # si elijo las tres
  if pollo.get()==1 and pizza.get()==1 and hamburguesa.get()==1:
    elegir+="""
    Tu orden final es: 
    -Pizza, 
    -Hamburguesa, 
    -Pollo"""
  imprimir.config(text=elegir) # se alamcena el resultado en imprimir

root=Tk()
root.geometry("400x300")

frame= Frame(root) # creo el frame para aca adentor tener los check buttons
frame.pack()

# Creo tres variables para uzar en el check button
pollo = IntVar()
pizza =  IntVar()
hamburguesa =  IntVar()

# los tres gif que tengo
#foto_pizza = PhotoImage(file="pizzas.gif")
#foto_hamburguesa = PhotoImage(file="burguer.gif")
#foto_pollo = PhotoImage(file="chien.gif")

# creo los tres label para empaquetar las imagenes
#Label(root, image=foto_pizza).pack()
#Label(root, image=foto_hamburguesa).pack()
#Label(root, image=foto_pollo).pack()

# Los tres check buttons con las opciones de comida a elegir
# onvalue es cuando esta seleciconado
# offvalue es cuando esta deseleccionado
Checkbutton(frame, text="Pizza", variable=pizza, onvalue=1, offvalue=0, command=eleccion).pack(side="right")
Checkbutton(frame, text="Hamburguesa", variable=hamburguesa, onvalue=1, offvalue=0, command=eleccion).pack(side="right")
Checkbutton(frame, text="Pollo", variable=pollo, onvalue=1, offvalue=0, command=eleccion).pack(side="right")

imprimir = Label(root) # para mostrar lo que el usuario elije
imprimir.pack()

root.mainloop()

