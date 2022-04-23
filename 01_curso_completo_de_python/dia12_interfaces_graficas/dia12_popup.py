from tkinter import*
from tkinter import filedialog

root=Tk()
root.title("Abrir")
root.geometry("400x300")

def abrir():
  archivo=filedialog.askopenfilename(title="Abrir", initialdir="Documentos", filetypes=( ("Documento Texto", "*.txt"), ("Documento Excel", "*.xlsx"))) 
  # initialdir="Documentos" asi abre desde documentos
  # filetypes=( ("Documento Texto", "*.txt"), ("Documento Excel", "*.xlsx") asi limito el tipo de archivo que puede abrir, puedo poner por ejemplo que sea .jpg o .png si quiero imagen
  print(archivo)

Button(root, text="Archivos", padx=10, pady=10, command=abrir).pack()

root.mainloop()