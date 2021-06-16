# Interfaz gráfica de usuario con widgets jerarquizados, 
# Tiene una raiz Tk, que es el elemento de mayor jerarquía y sobre este elemento se empieza a construir.


from tkinter import * # No orientado a objetos


# 1. Tk -> Este elemento es la raíz
root = Tk()   # EL primer elemento, esta ventana soporta .ico y bitmaps
root.title('Ventanita de Pajaritos')
#root.iconbitmap('bird.ico')  Linux no soporta .ico 
root.iconbitmap('@/home/isa/estudio/MinTIC/Python_MinTIC/week_6/bird.xbm') # porque es linux


# 2. Frame -> Marco
marco_1 = Frame(root)
marco_1.pack()
marco_1.config(border=10,background='blue')


# 3. Label -> Título o etiqueta
etiqueta_1 = Label(marco_1,text='Nombres') # Esta dentro del root
etiqueta_1.pack()  # Empacar en el tk con .pack() -> siempre hay que hacerlo


# 4. Entry   -> Campo de entrada
entrada_1 = Entry(marco_1)
entrada_1.pack()  # Si le pongo (side=LEFT) se va a la izquierda

# ----------------- #

marco_2 = Frame(root)
marco_2.pack()

etiqueta_2 = Label(marco_2, text='Apellidos')
etiqueta_2.pack()

entrada_2 = Entry(marco_2)
entrada_2.pack()
# ----------------- #


# Mainloop 
root.mainloop()  # Esto es lo segundo que se hace y es para crear la ventana. Debe ser al final del archivo para que no sse cierre la ventana.

