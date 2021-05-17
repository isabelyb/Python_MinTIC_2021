for x in range(0, 3):                      # for es cuando se sabeo se puede saber el número de iteraciones
    print(f"Estamos en la iteración {x}")

for x in range(0, 12, 2):                  # de 0 a 12, de a 2 
    print(f"Estamos en la iteración {x}")



contar = int(input("Cuántas notas vas a ingresar: "))

for nota in contar:
    print (int(input(f"Introduzca la nota: {nota} ")))
contar = int(input("Cuántas notas vas a ingresar: "))
promedio = total / contar
print( f"Promedio de notas del grado escolar: {promedio}")