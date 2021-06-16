#Otra forma de hacer las cosas sin el marco, con grilla (grid)

from tkinter import *


root = Tk()
root.title('Ventani')

etiqueta_1 = Label(root,text='Nombre')
etiqueta_1.grid(row=0, column=0)
entrada_1 = Entry(root)
entrada_1.grid(row=0, column=1)

etiqueta_2 = Label(root,text='Apellido')
etiqueta_2.grid(row=1, column=0)
entrada_2 = Entry(root)
entrada_2.grid(row=1, column=1)

root.mainloop()