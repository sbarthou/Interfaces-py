from tkinter import *
from tkinter.messagebox import *
root = Tk()
root.title('TKinter-py')


def muestra_ventana():
    respuesta = askquestion(message='¿Tu nombre es Juan?')   # respuesta guardará "yes" o "no"
    
    if respuesta == 'no':
        showinfo(message='¡No te llamas Juan!')
    else:
        respuesta_retry = askretrycancel(message='Haga click en "Retry" para reintentarlo')   # respuesta_retry guardará "True" o "False"
    
buton1 = Button(root, text='Enviar', command=muestra_ventana).pack()


root.mainloop()