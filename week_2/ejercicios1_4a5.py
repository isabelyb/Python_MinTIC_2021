numero = int(input("Ingrese un número: "))


def main():
    num_primo()
    
    
def num_primo():
    if numero > 0:
        num_primo_positivo()
    else:
        num_primo_negativo()


# 4.Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
def num_primo_positivo():
    contador = 0
    for divisor in range(1, numero + 1):
        if divisor == 1 or divisor == numero:
            continue
        if numero %divisor == 0:
            contador += 1
    if contador == 0:
        return print("4. Es primo")
    else:
        return print("4. No es primo")    


#5.Leer un número entero de dos dígitos y determinar si es primo y además si es negativo


def num_primo_negativo():
    contador = 0
    for divisor in range(numero, 0):
        if divisor == -1 or divisor == numero:
            continue
        if numero %divisor == 0:
            contador += 1
    if contador == 0:
        return print("5. Es primo y es negativo")
    else:
        return print("5. No es primo y es negativo") 



if __name__ == '__main__':
    main()