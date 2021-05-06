'''
Realizar un programa que calcule el puntaje de una persona que se postula a un empleo. 
La prueba consta de 50 preguntas. 
Realice una función que reciba como argumentos la cantidad de respuestas correctas, 
la cantidad de respuestas incorrectas y la cantidad de respuestas en blanco. 
Cada respuesta correcta representa 4 puntos. 
Cada respuesta incorrecta resta 1 punto y cada respuesta en blanco resta medio punto.
'''

def puntaje(correctas, incorrectas, en_blanco):
    puntaje_total = (correctas * 4) + (incorrectas * -1) + (en_blanco * -0.5)
    return puntaje_total

x = 10
y = 20
z = 20   

print(f"El puntaje de la persona es: {puntaje(x, y, z)} puntos")


def hello():
  name = str(input("Enter your name: "))
  if name:
    print ("Hello " + str(name))
  else:
    print("Hello World") 
  return 
  
hello()
