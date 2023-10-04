from tkinter import *

root = Tk()
root.resizable(0, 0)   # impide que usuario agrande ventana
root.geometry('300x320')   # establecer tamaño de ventana

def envia_numero(valor):
    anterior = pantalla.get()
    pantalla.delete(0, END)
    pantalla.insert(0, str(anterior) + str(valor))
    
def suma():
    global num1
    global op
    num1 = float(pantalla.get())
    pantalla.delete(0, END)
    op = '+'

def resta():
    global num1
    global op
    num1 = float(pantalla.get())
    pantalla.delete(0, END)
    op = '-'

def multiplicacion():
    global num1
    global op
    num1 = float(pantalla.get())
    pantalla.delete(0, END)
    op = 'x'
    
def division():
    global num1
    global op
    num1 = float(pantalla.get())
    pantalla.delete(0, END)
    op = '/'
    
def igual():
    global num2
    num2 = float(pantalla.get())
    pantalla.delete(0, END)
    if op == '+':
        pantalla.insert(0, num1 + num2)
    elif op == '-':
        pantalla.insert(0, num1 - num2)
    elif op == 'x':
        pantalla.insert(0, num1 * num2)
    elif op == '/':
        pantalla.insert(0, num1 / num2)

def clear():
    pantalla.delete(0, END)
    
pantalla = Entry(root, width=22, bg='black', fg='white', font=('menlo', 18))
pantalla.grid(row=0, padx=2, pady=2, columnspan=4)   # padx y pady: distancia borde , columnspan: número de columnas que ocupará

boton1 = Button(root, text='1', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(1)).grid(row=2, column=0, padx=1, pady=1)
boton2 = Button(root, text='2', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(2)).grid(row=2, column=1, padx=1, pady=1)
boton3 = Button(root, text='3', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(3)).grid(row=2, column=2, padx=1, pady=1)
boton4 = Button(root, text='4', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(4)).grid(row=3, column=0, padx=1, pady=1)
boton5 = Button(root, text='5', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(5)).grid(row=3, column=1, padx=1, pady=1)
boton6 = Button(root, text='6', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(6)).grid(row=3, column=2, padx=1, pady=1)
boton7 = Button(root, text='7', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(7)).grid(row=4, column=0, padx=1, pady=1)
boton8 = Button(root, text='8', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(8)).grid(row=4, column=1, padx=1, pady=1)
boton9 = Button(root, text='9', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(9)).grid(row=4, column=2, padx=1, pady=1)
boton0 = Button(root, text='0', width=4, height=3, bg='white', fg='black', cursor='hand2', command=lambda: envia_numero(0)).grid(row=5, column=0, padx=1, pady=1)

boton_igual = Button(root, text='=', width=4, height=3, bg='white', fg='blue', cursor='hand2', command=igual).grid(row=5, column=2, padx=1, pady=1)
boton_punto = Button(root, text='.', width=4, height=3, bg='white', fg='blue', cursor='hand2').grid(row=5, column=1, padx=1, pady=1)
boton_suma = Button(root, text='+', width=4, height=3, bg='white', fg='blue', cursor='hand2', command=suma).grid(row=2, column=3, padx=1, pady=1)
boton_resta = Button(root, text='-', width=4, height=3, bg='white', fg='blue', cursor='hand2', command=resta).grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text='x', width=4, height=3, bg='white', fg='blue', cursor='hand2', command=multiplicacion).grid(row=4, column=3, padx=1, pady=1)
boton_division = Button(root, text='/', width=4, height=3, bg='white', fg='blue', cursor='hand2', command=division).grid(row=5, column=3, padx=1, pady=1)
boton_clear = Button(root, text='clear', command=clear).grid(row=1)

root.mainloop()