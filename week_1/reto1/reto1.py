

def value_to_pay(name, last_name, value_insured, discount):
    print(f"The {name} {last_name}'s insurance value is: $ {sale_value_insurance} and the discount received is: $ {discount}")

'''
La función debe retornar una cadena de caracteres que le proporcione al asesor de seguros el
valor que debe pagar el tomador de acuerdo con el valor asegurado y el descuento otorgado
por la promoción del mes.
'''

name = 'Pedro'
last_name = 'Díaz'
value_insured = x = 10000000
discount = 5

value_insurance = (x*15)/100
discount_value = (value_insurance* discount) /100
sale_value_insurance = value_insurance - discount_value

value_to_pay(name, last_name, value_insured, discount_value)





