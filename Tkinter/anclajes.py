# Generar varios Radiobutton con ciclo for y lista de opciones
from tkinter import *
root = Tk()

def actualizar(valor):
    texto = Label(root, text=valor).pack()
    
titulo = Label(root, text="Selecciona una opción").pack()

opciones = [['Color rojo', 'rojo'],
            ['Color verde', 'verde'],
            ['Color azul', 'azul'],
            ['Color amarillo', 'amarillo']]

colores = StringVar()
colores.set('rojo')

for opcion, valor in opciones:
    Radiobutton(root, text=opcion, value=valor, variable=colores).pack(anchor=W)   # anchor: anclaje (N, NW, W, SW, S, SE, E NE)
    
boton_enviar = Button(root, text="Enviar", command=lambda: actualizar(colores.get())).pack()

root.mainloop()