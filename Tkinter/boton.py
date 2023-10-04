# entrada de usuario | boton enviar
from tkinter import *
root = Tk()

entrada = Entry(root, bg='black', fg='#A6A6A6')
entrada.grid(row=0, column=0)

def boton():
    texto = Label(root, text=entrada.get()).grid(row=2, column=0)
    
boton1 = Button(root, text="Enviar", command=boton).grid(row=1, column=0)   # grid se utiliza para posicionar el elemento en la fila y columna indicada

root.mainloop()