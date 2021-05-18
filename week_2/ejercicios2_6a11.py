numero = int(input("Digite un numero: "))
segundo_numero = int(input("Digite un segundo numero: "))
tercer_numero = int(input("Digite un tercer numero: "))
numero_3digitos = int(input("Ahora digite un numero de 3 dígitos: "))


def main():
    num_iguales()
    num_mayor()
    suma_digitos()
    posicion_mayor()
    multiplo()
    el_mayor()

# 6. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
def num_iguales():
    a_string = str(numero)
    if a_string[0] == a_string[1]:
        print("6. Los dos dígitos son iguales")
    else:
        print("6. Los dos dígitos no son iguales")


# 7. Leer dos números enteros y determinar cuál es el mayor.
def num_mayor():
    a_string = str(numero)
    if a_string[0] > a_string[1]:
        print("7. El primer dígito es mayor")
    elif a_string[0] < a_string[1]:
        print("7. El segundo dígito es mayor")
    else:
        print("7. Los dos dígitos son iguales")


#8. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.
def suma_digitos():
    a_string_1 = str(numero)
    a_string_2 = str(segundo_numero)
    suma_string = a_string_1 + a_string_2
    digitos = list(suma_string)  # convertir en lista
    for i in range(len(digitos)):
        digitos[i] = int(digitos[i]) # convertir en números
    total_suma = digitos[0] + digitos[1] + digitos[2] + digitos[3]
    print(f"8. La suma de todos los dígitos es: {total_suma}")


# 9. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
def posicion_mayor():
    a_string  = str(numero_3digitos)
    digitos = list(a_string)
    posicion = ""
    for i in range(len(digitos)):
        digitos[i] = int(digitos[i])
    if digitos[0] == digitos[1] and digitos[1] == digitos[2] and digitos[2] == digitos[0]:
        posicion = "9. Los tres dígitos son iguales"
    elif digitos[0] > digitos[1] and digitos[0] > digitos[2]:
        posicion = "9. El mayor dígito está en la primera posición"
    elif digitos[1] > digitos[0] and digitos[1] > digitos[2]:
        posicion = "9. El mayor dígito está en la segunda posición"
    else:
        posicion = "9. El mayor dígito está en la tercera posición"
    print(posicion)


# 10. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.
def multiplo():
    multiplo1()
    multiplo2()
    multiplo3()


def multiplo1():
    a_string  = str(numero_3digitos)
    digitos = list(a_string)
    multiplo1 = ""
    for i in range(len(digitos)):
        digitos[i] = int(digitos[i])
    if digitos[2] %digitos[0] == 0 or digitos[1] %digitos[0] == 0:
        if digitos[2] %digitos[0] == 0 and digitos[1] %digitos[0] == 0:
            multiplo1 = "10. Segundo y tercer dígitos son multiplos del primero"
        elif digitos[1] %digitos[0] == 0:
            multiplo1 = "10. El segundo dígito es multiplo del primero"
        else:
            multiplo1 = "10. El tercer dígito es multiplo del primero"
    print(multiplo1)


def multiplo2():
    a_string  = str(numero_3digitos)
    digitos = list(a_string)
    multiplo2 = ""
    for i in range(len(digitos)):
        digitos[i] = int(digitos[i])   
    if digitos[2] %digitos[1] == 0 or digitos[0] %digitos[1] == 0:
        if digitos[2] %digitos[1] == 0 and digitos[0] %digitos[1] == 0:
            multiplo2 = "10. Primer y tercer dígitos son multiplos del segundo"
        elif digitos[0] %digitos[1] == 0:
            multiplo2 = "10. El primer dígito es multiplo del segundo"
        else:
            multiplo2 = "10. El tercer dígito es multiplo del segundo"
    print(multiplo2)

def multiplo3():
    a_string  = str(numero_3digitos)
    digitos = list(a_string)
    multiplo3 = ""
    for i in range(len(digitos)):
        digitos[i] = int(digitos[i]) 
    if digitos[1] %digitos[2] == 0 or digitos[0] %digitos[2] == 0:
        if digitos[1] %digitos[2] == 0 and digitos[0] %digitos[2] == 0:
            multiplo3 = "10. Primer y segundo dígitos son multiplos del tercero"
        elif digitos[0] %digitos[2] == 0:
            multiplo3 = "10. El primer dígito es multiplo del tercero"
        else:
            multiplo3 = "10. El segundo dígito es multiplo del tercero"        
    print(multiplo3)

# 11. Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.
def el_mayor():
    primero = str(numero)
    segundo = str(segundo_numero)
    tercero = str(tercer_numero)
    todos = primero + segundo + tercero
    lista = list(todos)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    mayor = max(lista)
    if mayor in lista[0:2]:
        print("11. El mayor dígito se encuentra en el primer número")
    elif mayor in lista[2:4]:
        print("11. El mayor dígito se encuentra en el segundo número")
    else:
        print("11. El mayor dígito se encuentra en el tercer número")



if __name__ == '__main__':
    main()