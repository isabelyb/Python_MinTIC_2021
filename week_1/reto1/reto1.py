'''
Escriba una función qué reciba cómo parámetros: dos cadenas, una con el nombre del
tomador del seguro, y otra con el apellido (nombre, apellido), y dos números enteros, el valor
asegurado y el porcentaje de descuento de la promoción del mes (val_asegurado, descuento).
'''

def value_to_pay(name, last_name, value_insured, discount):
    print(f"The {name} {last_name}'s insurance value to pay is: $ {sale_value_insurance} and the discount received is: $ {discount}")

'''
La función debe retornar una cadena de caracteres que le proporcione al asesor de seguros el
valor que debe pagar el tomador de acuerdo con el valor asegurado y el descuento otorgado
por la promoción del mes.
'''

name = input("name: ")
last_name = input("last_name: ")
value_insured = int(input("type the value to insure: "))  # if the value is how the challenge, please type 5.
discount = int(input("How much is the discount to applicate?  "))

value_insurance = (value_insured*15)/100
discount_value = (value_insurance* discount) /100
sale_value_insurance = value_insurance - discount_value

value_to_pay(name, last_name, value_insured, discount_value)


# The challenge has to be in spanish and with the same structure that in the example:


def calcular_seguro(nombre, apellido, val_asegurado, descuento):
    valor_normal = (val_asegurado * 15) / 100
    valor_descuento = int((valor_normal * descuento) / 100)
    valor_total = int(valor_normal - valor_descuento)
    print(f"El valor del seguro de {nombre} {apellido} es: {valor_total}, el descuento realizado fue: {valor_descuento}")

calcular_seguro("Pedro", "Díaz", 10000000, 5)

 
 
