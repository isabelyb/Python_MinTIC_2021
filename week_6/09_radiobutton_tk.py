from tkinter import *

def select():
    etiqueta1.config(text=f'Usted escogió la opción {opcion.get()}')



root = Tk()
root.config(bd=20)
opcion = IntVar()


Radiobutton(root, text='Opción 1', variable=opcion, value=1, command=select).pack()


Radiobutton(root, text='Opción 2', variable=opcion, value=2, command=select).pack()


Radiobutton(root, text='Opción 3', variable=opcion, value=3, command=select).pack()

etiqueta1 = Label(root)
etiqueta1.pack()

root.mainloop()