# Raddiobutton, guarda input ingresado y lo muestra en pantalla
from tkinter import *
root = Tk()

x = IntVar()   # variable número entero

def actualizar(valor):   # funcion que actualiza el texto que se muestra según la opción marcada
    texto = Label(root, text=valor).grid(row=3)

titulo = Label(root, text="Selecciona una opción").grid(row=0)

opcion1 = Radiobutton(root, text="Opción 1", value=1, variable=x, command=lambda: actualizar(x.get())).grid(row=1)
opcion2 = Radiobutton(root, text="Opción 2", value=2, variable=x, command=lambda: actualizar(x.get())).grid(row=2)

root.mainloop()