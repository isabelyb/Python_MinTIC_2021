"""21. Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y
5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó
o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro
del rango permitido.
"""

def main():
    calificacion()

def calificacion():
    total = 0
    for nota in range(0, 3):
        notas = float(input(f"Por favor digite su nota {nota + 1}: "))    
        if notas < 0 or notas > 5:
            print("Su nota debe estar entre 0 y 5")
            notas = float(input(f"Por favor digite nuevamente la nota: "))
        total = total + notas 
        promedio = total / 3
    
    if promedio > 3:
        print(f"Su promedio ha sido {promedio} y ha APROBADO")
    else:
        print(f"Su promedio ha sido {promedio}, ha REPROBADO")




if __name__ == '__main__':
    main()