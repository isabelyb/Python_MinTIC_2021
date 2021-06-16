from tkinter import *

def seleccionar():
    pass

root = Tk()
root.config(bd=20)
choco = IntVar()
fruta = IntVar()
image1 = PhotoImage(file='/home/isa/estudio/MinTIC/Python_MinTIC/week_6/icecream.gif')
Label(root, image=image1).pack()

marco1 = Frame(root)
marco1.pack()

marco1= Frame(root)
marco1.pack()


Checkbutton(marco1, text='Con chocolate', variable=choco, onvalue=1, offvalue=0, command=seleccionar).pack()

Checkbutton(marco1, text='Con frutas', variable=fruta, onvalue=1, offvalue=0, command=seleccionar).pack()


root.mainloop()