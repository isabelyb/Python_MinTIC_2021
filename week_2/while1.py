promedio = 0.0
total = 0
contar = 0
mensaje = ("Introduzca la nota de un estudiante (-1 para salir): ")
grado = int(input(mensaje))

while grado != -1:            # Condición
    total = total + grado     # Acumulador
    contar += 1               # Contador
    grado = int(input(mensaje))
else:
    promedio = total / contar
    print("Promedio de notas del grado escolar: " + str(promedio))
    print( f"Promedio de notas del grado escolar: {promedio}")  # otra forma de imprimir el string