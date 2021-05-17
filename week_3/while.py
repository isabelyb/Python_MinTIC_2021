# Conteo regresivo de 5 a 1

n = 5          # inicialización de la variable
while n > 0:   # concdición
    print(n)   # cuerpo
    n = n - 1  # Avance
print("¡Despegue!")


#  Imprimir de 1 a 10

n = 1          # inicialización de la variable
while n < 11:  # condición
    print(n)   # cuerpo
    n = n + 1  # Avance


#  Imprimir de 10 a 1

n = 10         # inicialización de la variable
while n > 0:   # condición
    print(n)   # cuerpo
    n = n - 1  # Avance


# Bucle while controlado por un evento

promedio = 0.0
total = 0
contar = 0

print("Introduzca la nota de un estudiante (-1 para salir): ")

grado = int(input())

while grado != -1:
    total = total + grado   # Variable acumuladora
    contar = contar + 1     # Variable Contador
    print("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
promedio = (total / contar)
print("Promedio de notas del grado escolar es: " + str(promedio))