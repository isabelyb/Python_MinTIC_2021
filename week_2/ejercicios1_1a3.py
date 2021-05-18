numero = int(input("Ingrese un número: "))


def main():
    num_term_4()
    num_3_cifras()
    num_dos_digitos_pares()
    

# 1.Leer un número entero y determinar si es un número terminado en 4. 
def num_term_4():
    en_string = str(numero)
    ultimo_digito = en_string[-1]
    if ultimo_digito == "4":
        print ("1. El número termina en 4")
    else:
        print ("1. El número no termina en 4")
    

# 2.Leer un número entero y determinar si tiene 3 dígitos.
def num_3_cifras():
    en_string = str(numero)
    longitud = len(en_string)
    if longitud == 3:
        print ("2. El número tiene 3 dígitos")
    else:
        print ("2. El número no tiene 3 dígitos")


# 3.Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
def num_dos_digitos_pares():
    en_string = str(numero)
    ultimo_digito = en_string[-1]
    primer_digito = en_string[0]
    ultimo_numero = int(ultimo_digito)
    primer_numero = int(primer_digito)
    if  primer_numero %2 == 0 and ultimo_numero %2 == 0:
        print("3. Ambos dígitos son pares")
    else:
        print("3. Ambos dígitos no son pares")


if __name__ == '__main__':
    main()