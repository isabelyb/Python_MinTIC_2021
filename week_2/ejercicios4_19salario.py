"""19. A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. Si la
cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las
horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la tarifa
ingresadas por el usuario.
"""

def main():
    calcular_salario()

def calcular_salario():
    horas_trabajadas = int(input("Cuántas horas trabajó: "))
    tarifa = int(input("Cual es la tarifa de la hora? (solo valor): "))
    tarifa_extra = tarifa + ((tarifa*50)/100)
    horas_extras = horas_trabajadas - 40
    salario = ""

    if horas_trabajadas <= 40:
        salario = horas_trabajadas * tarifa
    else:
        salario = (horas_extras * tarifa_extra) + (40 * tarifa)
    
    print(f"Tu salario es: {salario} pesos")
    

if __name__ == '__main__':
    main()