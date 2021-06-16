# from turtle import *  # No orientada a objetos

# #Ventana pa dibujar
# setup(400,300,900,100)  #ancho, alto, donde la voy a dibujar
# #showturtle() mostar
# #hideturtle() ocultar
# goto(150,0)  # muestra puntero
# goto(0,120)
# goto(0,0)

# mainloop()

import turtle # orientada a objetos

a = turtle

#Ventana pa dibujar
a.setup(400,300,900,100)  #ancho, alto, donde la voy a dibujar
a.showturtle()
#hideturtle()
a.colormode(255)
a.pensize(4)
a.begin_fill()
a.fillcolor('yellow')
a.pencolor(255,0,0) #rojo
#a.color('pink')

# Triángulo
a.goto(150,0)  # muestra puntero
a.pencolor(0,255,0)
a.goto(0,120)
a.pencolor(0,0,255)
a.goto(0,0)
a.end_fill()

# Cuadrado
a.color('pink')
a.penup()
a.goto(-50,0)
a.pendown()
a.goto(-150,0)
a.goto(-150,-100)
a.goto(-50,-100)
a.goto(-50,0)


a.exitonclick() 


# Geyden Tamayo  -> No me sale nada
a.penup()
a.forward(50)
a.pendown()
a.left(90)
a.forward(50)
a.left(90)
a.forward(50)
a.left(90)
a.forward(50)
a.left(90)

a.exitonclick() 


a.mainloop()
