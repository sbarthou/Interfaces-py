from tkinter import *
from tkinter.messagebox import *
root = Tk()
root.title('messagebox.py')

def ventana_question():
    askquestion(title='título de la ventana', message='¿pregunta?')
    
def ventana_yesno():
    askyesno(title='título de la ventana', message='yes or no?')
    
def ventana_yesnocancel():
    askyesnocancel(title='título de la ventana', message='yes, no or cancel?')

def ventana_retrycancel():
    askretrycancel(title='título de la ventana', message='¿pregunta?')
    
boton1 = Button(root, text='question', command=ventana_question).pack()
boton2 = Button(root, text='yes no', command=ventana_yesno).pack()
boton3 = Button(root, text='yes no cancel', command=ventana_yesnocancel).pack()
boton4 = Button(root, text='retry cancel', command=ventana_retrycancel).pack()

root.mainloop()