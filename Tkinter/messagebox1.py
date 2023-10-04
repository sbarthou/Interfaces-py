from tkinter import *
from tkinter.messagebox import *
root = Tk()
root.title('messagebox.py')

def ventana_info():
    showinfo(title='título de la ventana', message='mensaje que se muestra en la ventana')
    
def ventana_warning():
    showwarning(title='título de la ventana', message='mensaje que se muestra en la ventana')
    
def ventana_error():
    showerror(title='título de la ventana', message='mensaje que se muestra en la ventana')
    
boton1 = Button(root, text='info', command=ventana_info).pack()
boton2 = Button(root, text='warning', command=ventana_warning).pack()
boton3 = Button(root, text='error', command=ventana_error).pack()

root.mainloop()