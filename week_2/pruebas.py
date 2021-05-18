# # Para conocer el último dígito:
# numero = 1235654

# letras = str(numero)
# print(letras)

# longitud = len(letras)
# print(longitud)

# ultimo = letras[-1]
# primero = letras[0]
# print(ultimo)
# print(primero)

# print (ultimo == "4")
# print (ultimo == "8")

numero = 18

def num_primo():
    divisor = 1
    while divisor != 1 and divisor != numero and divisor < 20:
        numero / divisor
        divisor += 1
        if numero %divisor == 0:
            print("No es primo")
        else:
            print("Es primo")


print(num_primo())


# def num():
#     try:
#         if numero > 5:
#             print("numero > 5")
#         else:
#             print ("numero < 5")
#     except:
#         print("inserte un numero")




# temperatura_fahr = input('Enter Fahrenheit Temperature:')
# try:
#     fahr = float(temperatura_fahr)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Please enter a number')