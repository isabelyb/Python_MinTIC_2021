# 12. Leer un número entero de suma de los otros dos.
    #No entendí este problema.

numero_menor_que_50 = int(input("Número menor que 50: "))
numero_4_digitos = int(input("Número de 4 dígitos: "))
numero_entero = int(input("Número entero: "))
numero_entero2 = int(input("Otro Número entero: "))
numero_entero3 = int(input("Otro Número entero: "))

def main():
    es_primo()
    numero_igual()
    multiplo_7()
    cuantos_digitos()
    pares_impares()
    ultimo_igual()

# 13. Leer un número entero menor que 50 y positivo y determinar si es un número primo.
def es_primo():
    if numero_menor_que_50 < 50:
        contador = 0
        for divisor in range(1, numero_menor_que_50  + 1):
            if divisor == 1 or divisor == numero_menor_que_50:
                continue
            if numero_menor_que_50 %divisor == 0:
                contador += 1
        if contador == 0:
            return print(f"13. {numero_menor_que_50} Es primo")
        else:
            return print(f"13. {numero_menor_que_50} No es primo")
    else:
        print(f"13. {numero_menor_que_50} no es menor que 50")
            

# 14. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.
def numero_igual():
    a_string = str(numero_4_digitos)
    numeros = list(a_string)
    for numero in range(len(numeros)):
        numeros[numero] = int(numeros[numero])
    
    if numeros[1] == numeros[2]:
        print("14. El segundo dígito es igual al penúltimo")
    else:
        print("14. El segundo dígito y el penúltimo son diferentes")


# 15. Leer un número entero y determinar si es múltiplo de 7.
def multiplo_7():
    if numero_entero %7 == 0:
        print(f"15. {numero_entero} es múltiplo de 7")
    else:
        print(f"15. {numero_entero} no es múltiplo de 7")


# 16. Leer un número entero menor que mil y determinar cuántos dígitos tiene.
def cuantos_digitos():
    a_string = str(numero_entero)
    digitos = list(a_string)
    cuantos = len(digitos)
    print(f"16. {numero_entero} tiene {cuantos} dígitos")


# 17. Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.
def pares_impares():
    a_string = str(numero_4_digitos)
    numeros = list(a_string)
    
    for i in range(len(numeros)):
        numeros[i] = int(numeros[i])
    
    pares = 0
    impares = 0
    for i in range(len(numeros)):
        if  numeros[i] %2 == 0:
            pares += 1
        else:
            impares += 1

    if pares > impares:
        print (f"17. {numero_4_digitos} tiene mas números pares")
    elif pares < impares:
        print (f"17. {numero_4_digitos} tiene mas números impares")
    else:
        print (f"17. {numero_4_digitos} tiene igual números pares e impares")



# 18. Leer tres números enteros y determinar si el último dígito de los tres números es igual.
def ultimo_igual():
    a_string1 = str(numero_entero)
    a_string2 = str(numero_entero2)
    a_string3 = str(numero_entero3)

    numero1 = list(a_string1)
    numero2 = list(a_string2)
    numero3 = list(a_string3)

    ultimo1 = int(numero1[-1])
    ultimo2 = int(numero2[-1])
    ultimo3 = int(numero3[-1])

    if ultimo1 == ultimo2 and ultimo2 == ultimo3:
        print("18. Los últimos dígitos de los tres números son iguales")
    else:
        print("18. Los últimos dígitos de los tres números no son iguales") 


if __name__ == '__main__':
    main()






