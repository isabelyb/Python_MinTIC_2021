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


# lista = [2,5,8,9,6,1]
# mayor = max(lista)
# print(mayor in lista[2:3])

# palabra = "hola"
# lista = list(palabra)
# print(lista)

# palabra_nueva = str(lista)
# print(palabra_nueva)

datos_tanque = {
'codigoTanque': 'TA001',
'sensor1':'estado',
'sensor2':'estado',
'sensor3':'estado'
}

print(datos_tanque['codigoTanque'])

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