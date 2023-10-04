# Generar varios Radiobutton con ciclo for y lista de opciones
from tkinter import *
root = Tk()

def actualizar(valor):
    texto = Label(root, text=valor).pack()
    
titulo = Label(root, text="Selecciona una opción").pack()

opciones = [['Color rojo', 'rojo'],   # el primer elemento serámel que aparece en pantalla y el segundo el que se envía al programa
            ['Color verde', 'verde'],
            ['Color azul', 'azul'],
            ['Color amarillo', 'amarillo']]

colores = StringVar()   # usamos StrinVar() (variable de control) porque los datos que se estarán enviando son strings
colores.set('rojo')   # predefinir un valor

for opcion, valor in opciones:
    Radiobutton(root, text=opcion, value=valor, variable=colores).pack()
    
boton_enviar = Button(root, text="Enviar", command=lambda: actualizar(colores.get())).pack()

root.mainloop()