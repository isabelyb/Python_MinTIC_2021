#variables de control:
#entero = IntVar()  # Declara variable de tipo entera
#flotante = DoubleVar()  # Declara variable de tipo flotante
#cadena = StringVar()  # Declara variable de tipo cadena
#booleano = BooleanVar()  # Declara variable de tipo booleana

from tkinter import *

def sumar():
    result.set(float(num1.get())+float(num2.get()))


def restar():
    result.set(float(num1.get())-float(num2.get()))
    borrar()


def multiplicar():
    result.set(float(num1.get())*float(num2.get()))
    borrar()

def dividir():
    result.set(float(num1.get())/float(num2.get()))
    borrar()

def borrar():
    num1.set('')
    num2.set('')

root = Tk()
root.title('Calculadora')
root.config(bd=20)
num1 = StringVar()
num2 = StringVar()
result= StringVar()
#etiqueta1 = Label(root, text='Número 1')
#etiqueta1.pack()
Label(root,text='Número 1').pack()
Entry(root, textvariable=num1).pack()

Label(root,text='Número 2').pack()
Entry(root, textvariable=num2).pack()

Label(root,text='Resultado').pack()
Entry(root, textvariable=result, state='disable').pack()

Button(root, text=' + ', command=sumar).pack()
Button(root, text=' - ', command=restar).pack()
Button(root, text=' * ', command=multiplicar).pack()
Button(root, text=' / ', command=dividir).pack()




root.mainloop()
