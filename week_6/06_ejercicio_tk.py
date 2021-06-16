from tkinter import *


def imprimir():
    etiqueta1.config(text='Hola Mundo')

def borrar():
    etiqueta1.config(text='')

root = Tk()
root.title('Botón')
root.config(bd=20)



boton1 = Button(root, text='Imprimir', command=imprimir)
boton1.pack()

boton2 = Button(root, text='Borrar', command=borrar)
boton2.pack()

etiqueta1 = Label(root)
etiqueta1.pack()


root.mainloop()